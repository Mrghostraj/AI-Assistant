import os
import time
import subprocess


SAMPLE_RATE = 16000
CHANNELS = 1

NUM_SAMPLES = 100
RECORD_DURATION = 1.5

OUTPUT_DIR = "wakeword/positive"


os.makedirs(OUTPUT_DIR, exist_ok=True)


def record_sample(output_file):

    command = [
        "ffmpeg",
        "-y",
        "-f", "pulse",
        "-i", "default",
        "-ac", str(CHANNELS),
        "-ar", str(SAMPLE_RATE),
        "-t", str(RECORD_DURATION),
        "-c:a", "pcm_s16le",
        output_file
    ]

    subprocess.run(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )


print("=" * 45)
print("        AIRA WAKE WORD RECORDER")
print("=" * 45)

print(f"\nWe will record {NUM_SAMPLES} samples.")
print("For every sample, say: Aira")
print("Try to vary your voice naturally.")
print("\nPress ENTER to start...\n")

input()


for i in range(1, NUM_SAMPLES + 1):

    output_file = os.path.join(
        OUTPUT_DIR,
        f"aira_{i:03d}.wav"
    )

    print(f"\n[{i}/{NUM_SAMPLES}] Get ready...")

    time.sleep(1)

    print("🎤 Say: Aira")

    record_sample(output_file)

    print(f"✅ Saved: {output_file}")

    if i < NUM_SAMPLES:
        print("Next recording in 1 second...")
        time.sleep(1)


print("\n" + "=" * 45)
print("All recordings completed!")
print(f"Saved in: {OUTPUT_DIR}")
print("=" * 45)