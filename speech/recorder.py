import numpy as np
import subprocess
from collections import deque

from speech.vad import VoiceActivityDetector


sample_rate = 16000
channels = 1
chunk_size = 512

speech_threshold = 0.5
silence_duration = 1

pre_buffer_duration = 0.2


def read_exact(stream, size):

    data = bytearray()

    while len(data) < size:

        chunk = stream.read(size - len(data))

        if not chunk:
            return None

        data.extend(chunk)

    return bytes(data)


def record_audio():

    vad = VoiceActivityDetector()

    command = [
        "ffmpeg",
        "-loglevel", "error",
        "-f", "pulse",
        "-i", "default",
        "-ac", str(channels),
        "-ar", str(sample_rate),
        "-f", "f32le",
        "pipe:1"
    ]

    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        bufsize=0
    )

    audio_chunks = []

    speech_started = False
    silence_chunks = 0

    silence_limit = int(
        silence_duration * sample_rate / chunk_size
    )

    pre_buffer_size = int(
        pre_buffer_duration * sample_rate / chunk_size
    )

    pre_buffer = deque(
        maxlen=pre_buffer_size
    )

    print("Listening....")

    try:

        while True:

            audio_bytes = read_exact(
                process.stdout,
                chunk_size * 4
            )

            if audio_bytes is None:
                break

            audio_chunk = np.frombuffer(
                audio_bytes,
                dtype=np.float32
            ).copy()

            probability = vad.is_speech(
                audio_chunk,
                sample_rate
            )

            # -------------------------
            # Speech detected
            # -------------------------

            if probability >= speech_threshold:

                if not speech_started:

                    print("Speech detected....")

                    # Add audio recorded
                    # just before speech detection
                    audio_chunks.extend(
                        list(pre_buffer)
                    )

                speech_started = True
                silence_chunks = 0

                audio_chunks.append(
                    audio_chunk
                )

            # -------------------------
            # Silence detected
            # -------------------------

            else:

                if speech_started:

                    audio_chunks.append(
                        audio_chunk
                    )

                    silence_chunks += 1

                    if silence_chunks >= silence_limit:

                        print("Speech Ended....")
                        break

                else:

                    # Keep recent silence/audio
                    # available as pre-buffer
                    pre_buffer.append(
                        audio_chunk
                    )

    except KeyboardInterrupt:

        print("\nRecording stopped.")

    finally:

        process.terminate()
        process.wait()

    if not audio_chunks:

        return np.array([], dtype=np.float32)

    return np.concatenate(audio_chunks)