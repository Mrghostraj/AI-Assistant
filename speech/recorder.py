import numpy as np 
import subprocess

sample_rate = 16000
channels = 1

def record_audio(duration=10):
    command = [
        "ffmpeg",
        "-f", "pulse",
        "-i", "default",
        "-ac", str(channels),
        "-ar", str(sample_rate),
        "-f", "f32le",
        "-t", str(duration),
        "pipe:1"
    ]

    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )

    audio_bytes, _ = process.communicate()

    audio = np.frombuffer(
        audio_bytes,
        dtype = np.float32
    )

    return audio

if __name__ == "__main__":
    audio = record_audio()

    print("Audio Captured succesfuly!")
    print("Shape:", audio.shape)
    print("datatype:", audio.dtype)
    print("Duration:", len(audio) / sample_rate, "seconds")
