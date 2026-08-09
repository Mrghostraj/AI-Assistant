import subprocess 
import numpy as np 
from speech.vad import VoiceActivityDetector

sample_rate = 16000
chunk_size = 512 

vad = VoiceActivityDetector()

command =[
    "ffmpeg",
    "-f", "pulse",
    "-i", "default",
    "-ac", "1",
    "-ar", str(sample_rate),
    "-f", "f32le",
    "pipe:1"
]

process = subprocess.Popen(
    command,
    stdout=subprocess.PIPE,
    stderr= subprocess.DEVNULL
)

print("Speak Now....")
print("Press Ctrl+C to stop.\n")

try:

    while True:
        audio_bytes = process.stdout.read(chunk_size*4)

        if len(audio_bytes) < chunk_size *4:
            break 

        audio_chunk = np.frombuffer(audio_bytes, dtype=np.float32)

        probability = vad.is_speech(audio_chunk, sample_rate)

        if probability >=0.5:
            status = "Speech"
        else:
            status = "Silence"

        print(f"{status} | Probability: {probability:.3f}")

except KeyboardInterrupt:
    print("\nStopping....")

finally:
    process.terminate()
    process.wait()