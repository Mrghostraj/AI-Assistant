from speech.speech_to_text import speechtotext
from speech.recorder import record_audio
from speech.Text_to_speech import texttospeech
from llm.ollama_client import ask


# ============================================================
# INITIALIZE MODELS
# ============================================================

stt = speechtotext(model_size="small")

tts = texttospeech(
    "./voices/en_US-lessac-medium.onnx",
    "./voices/hi_IN-pratham-medium.onnx"
)


# ============================================================
# CONFIGURATION
# ============================================================

EXIT_COMMANDS = [
    "exit",
    "quit",
    "stop",
    "bye",
    "goodbye",
    "band karo",
    "band kar do",
    "bas",
]


# ============================================================
# MAIN ASSISTANT
# ============================================================

def main():

    print("=" * 50)
    print("        AIRA AI ASSISTANT")
    print("=" * 50)
    print("Aira is ready!")
    print("Speak naturally. Say 'exit' or 'bye' to stop.")
    print("=" * 50)

    conversation_history = []

    while True:

        # ----------------------------------------------------
        # RECORD USER AUDIO
        # ----------------------------------------------------

        print("\n🎤 Speak Now...")

        try:
            audio = record_audio()
        except Exception as e:
            print("Recording error:", e)
            continue


        # ----------------------------------------------------
        # SPEECH TO TEXT
        # ----------------------------------------------------

        try:
            text, info = stt.transcribe(audio)
        except Exception as e:
            print("STT error:", e)
            continue


        # ----------------------------------------------------
        # EMPTY INPUT
        # ----------------------------------------------------

        if not text or not text.strip():

            print("I didn't understand you.")
            continue


        text = text.strip()

        print("\nYou:", text)
        print("Language:", info.language)
        print("Probability:", info.language_probability)


        # ----------------------------------------------------
        # EXIT COMMAND
        # ----------------------------------------------------

        text_lower = text.lower()

        if any(command in text_lower for command in EXIT_COMMANDS):

            goodbye = "Okay, talk to you later!"

            print("\nAssistant:", goodbye)

            try:
                tts.speak(goodbye, info.language)
            except Exception as e:
                print("TTS error:", e)

            break


        # ----------------------------------------------------
        # SEND TO LLM
        # ----------------------------------------------------

        try:

            response = ask(
                text,
                conversation_history
            )

        except TypeError:

            # In case your current ask() only accepts
            # one argument
            response = ask(text)

        except Exception as e:

            print("LLM error:", e)
            continue


        # ----------------------------------------------------
        # DISPLAY RESPONSE
        # ----------------------------------------------------

        print("\nAssistant:", response)


        # ----------------------------------------------------
        # SAVE CONVERSATION
        # ----------------------------------------------------

        conversation_history.append({
            "role": "user",
            "content": text
        })

        conversation_history.append({
            "role": "assistant",
            "content": response
        })


        # ----------------------------------------------------
        # TEXT TO SPEECH
        # ----------------------------------------------------

        try:

            tts.speak(
                response,
                info.language
            )

        except Exception as e:

            print("TTS error:", e)


# ============================================================
# START
# ============================================================

if __name__ == "__main__":
    main()