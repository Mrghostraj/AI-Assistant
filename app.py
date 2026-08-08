from speech.speech_to_text import speechtotext
from speech.recorder import record_audio
from speech.Text_to_speech import texttospeech
from llm.ollama_client import ask

stt = speechtotext(model_size="base")
tts = texttospeech(
    "./voices/en_US-lessac-medium.onnx"
)

def main():
    print("Your AI-Assistant is ready!")

    print("\nSpeak Now....")

    audio= record_audio(duration=10)

    text, info = stt.transcribe(audio)


    print("Language:", info.language)
    print("\nYou:", text)


    if not text:
        print("I didnot Understand You.")
        return

    response = ask(text)

    print("\n Assistant:", response)

    output_file = tts.speak(response)

    print("Audio saved:", output_file)


if __name__ == "__main__":
    main()

