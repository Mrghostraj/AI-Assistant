from speech.speech_to_text import speechtotext
from speech.recorder import record_audio

stt = speechtotext(model_size="base")

print("Speak Now....")
audio_file = record_audio(duration=10)

text, info = stt.transcribe(audio_file)

print("\nDetected Language:", info.language)
print("Transcription:", text)
