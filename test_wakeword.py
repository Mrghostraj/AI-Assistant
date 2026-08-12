import numpy as np
import subprocess
from openwakeword.model import Model


SAMPLE_RATE = 16000
CHUNK_SIZE = 1280

model = Model(
    wakeword_models=["hey_jarvis"]
)

print("Wake word detector ready!")
print("Say: Hey Jarvis")


command = [
    "ffmpeg",
    "-f", "pulse",
    "-i", "default",
    "-ac", "1",
    "-ar", str(SAMPLE_RATE),
    "-f", "s16le",
    "pipe:1"
]

process = subprocess.Popen(
    command,
    stdout=subprocess.PIPE,
    stderr=subprocess.DEVNULL
)

count = 0
try:

    while True:
    
        audio_bytes = process.stdout.read(
            CHUNK_SIZE * 2
        )
    
        if len(audio_bytes) < CHUNK_SIZE * 2:
            break
        
        count += 1
    
        if count % 100 == 0:
            print("Receiving audio...")
    
        audio = np.frombuffer(
            audio_bytes,
            dtype=np.int16
        )
    
        prediction = model.predict(audio)
    
        score = prediction["hey_jarvis"]
    
        if score > 0.5:
            print("🔥 Wake word detected!")
            print("Score:", score)

finally:

    process.terminate()
    process.wait()