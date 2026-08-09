from speech.recorder import record_audio
from speech.speech_to_text import speechtotext
import soundfile as sf


print("Speak now...")

audio = record_audio()

sf.write(
    "hindi_test_stt.wav",
    audio,
    16000
)

print("Audio saved.")

stt = speechtotext(model_size="small")

text, info = stt.transcribe(audio)

print("Language:", info.language)
print("Text:", text)