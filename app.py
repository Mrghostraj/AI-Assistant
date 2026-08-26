from speech.speech_to_text import speechtotext
from speech.recorder import record_audio
from speech.Text_to_speech import texttospeech

from llm.ollama_client import ask

from tools.task_handler import handle_task


# ============================================================
# INITIALIZE MODELS
# ============================================================

stt = speechtotext(
    model_size="small"
)


tts = texttospeech(
    "./voices/en_US-lessac-medium.onnx",
    "./voices/hi_IN-pratham-medium.onnx"
)


# ============================================================
# CONFIGURATION
# ============================================================

EXIT_COMMANDS = [
    "bye",
    "goodbye",
    "exit",
    "quit",
    "stop"
]


# ============================================================
# MAIN
# ============================================================

def main():

    print("=" * 50)
    print("        AIRA AI ASSISTANT")
    print("=" * 50)

    print(
        "Aira is ready!"
    )

    print(
        "Speak naturally. Say 'exit' or 'bye' to stop."
    )

    print("=" * 50)


    # Conversation memory

    conversation_history = []


    # ========================================================
    # CONVERSATION LOOP
    # ========================================================

    while True:


        # ----------------------------------------------------
        # RECORD AUDIO
        # ----------------------------------------------------

        print("\n🎤 Speak Now...")

        try:

            audio = record_audio()

        except Exception as e:

            print(
                "Recording error:",
                e
            )

            continue


        # ----------------------------------------------------
        # SPEECH TO TEXT
        # ----------------------------------------------------

        try:

            text, info = stt.transcribe(
                audio
            )

        except Exception as e:

            print(
                "STT error:",
                e
            )

            continue


        # ----------------------------------------------------
        # EMPTY INPUT
        # ----------------------------------------------------

        if not text or not text.strip():

            print(
                "I didn't understand you."
            )

            continue


        text = text.strip()


        # ----------------------------------------------------
        # DISPLAY STT RESULT
        # ----------------------------------------------------

        print(
            "\nYou:",
            text
        )

        print(
            "Language:",
            info.language
        )

        print(
            "Probability:",
            info.language_probability
        )


        # ----------------------------------------------------
        # EXIT
        # ----------------------------------------------------

        text_lower = text.lower()


        if any(
            command in text_lower
            for command in EXIT_COMMANDS
        ):

            goodbye = (
                "Okay, talk to you later!"
            )

            print(
                "\nAssistant:",
                goodbye
            )


            try:

                tts.speak(
                    goodbye,
                    info.language
                )

            except Exception as e:

                print(
                    "TTS error:",
                    e
                )

            break


        # ----------------------------------------------------
        # TASK HANDLER
        # ----------------------------------------------------

        try:

            task_response = handle_task(
                text
            )

        except Exception as e:

            print(
                "Task error:",
                e
            )

            task_response = None


        # ----------------------------------------------------
        # TASK FOUND
        # ----------------------------------------------------

        if task_response:

            response = task_response


        # ----------------------------------------------------
        # NORMAL LLM CONVERSATION
        # ----------------------------------------------------

        else:

            try:

                response = ask(
                    text,
                    conversation_history
                )

            except Exception as e:

                print(
                    "LLM error:",
                    e
                )

                continue


        # ----------------------------------------------------
        # DISPLAY RESPONSE
        # ----------------------------------------------------

        print(
            "\nAssistant:",
            response
        )


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

            print(
                "TTS error:",
                e
            )


# ============================================================
# START
# ============================================================

if __name__ == "__main__":

    main()