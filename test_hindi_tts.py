from piper import PiperVoice
import wave

voice = PiperVoice.load(
    "./voices/hi_IN-pratham-medium.onnx"
)

text = "नमस्ते, मेरा नाम रंधीर कुमार है। आज हम एक AI असिस्टेंट बना रहे हैं।"

with wave.open("hindi_test.wav", "wb") as wav_file:
    voice.synthesize_wav(text, wav_file)

print("Hindi audio generated.")