from piper import PiperVoice
import wave


text = """ नमस्ते, मेरा नाम रंधीर है और मैं एक पर्सनल AI असिस्टेंट बना रहा हूँ।
यह असिस्टेंट मेरी आवाज़ को समझ सकता है, मेरे सवालों का जवाब दे सकता है
और अलग-अलग कामों में मेरी मदद कर सकता है।
मैं चाहता हूँ कि यह असिस्टेंट हिंदी और अंग्रेज़ी दोनों भाषाओं में
स्वाभाविक तरीके से बातचीत कर सके।
"""

voices = {
    "pratham": "./voices/hi_IN-pratham-medium.onnx",
    "priyamvada": "./voices/hi_IN-priyamvada-medium.onnx",
    "rohan": "./voices/hi_IN-rohan-medium.onnx",
}


for name, path in voices.items():

    print(f"Generating {name}...")

    voice = PiperVoice.load(path)

    output_file = f"{name}_test.wav"

    with wave.open(output_file, "wb") as wav_file:
        voice.synthesize_wav(
            text,
            wav_file
        )

    print(f"Saved: {output_file}")