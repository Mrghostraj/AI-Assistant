from speech.speech_to_text import speechtotext
from speech.recorder import record_audio
from speech.Text_to_speech import texttospeech
from llm.ollama_client import ask
from tools.task_handler import handle_task

stt = speechtotext(
    model_size="small"
)

tts = texttospeech(
    "./voices/en_US-lessac-medium.onnx",
    "./voices/hi_IN-pratham-medium.onnx"
)

EXIT_COMMANDS = [
    "bye",
    "goodbye",
    "exit",
    "quit",
    "stop"
]

def is_exit_command(text):

    text = text.lower().strip()

    return any(
        command in text
        for command in EXIT_COMMANDS
    )


def listen():

    try:

        print("\n🎤 Speak Now...")

        audio = record_audio()

        text, info = stt.transcribe(
            audio
        )

        if not text or not text.strip():

            return None, None

        text = text.strip()

        print("\nYou:", text)

        print(
            "Language:",
            info.language
        )

        print(
            "Probability:",
            info.language_probability
        )

        return text, info

    except Exception as e:

        print(
            "Speech error:",
            e
        )

        return None, None


def generate_response(
    text,
    conversation_history
):

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


    if task_response:

        return task_response


    try:

        return ask(
            text,
            conversation_history
        )

    except Exception as e:

        print(
            "LLM error:",
            e
        )

        return None


def save_conversation(
    history,
    user_text,
    assistant_text
):

    history.append({

        "role": "user",

        "content": user_text

    })

    history.append({

        "role": "assistant",

        "content": assistant_text

    })


def speak_response(
    response,
    language
):

    try:

        tts.speak(
            response,
            language
        )

    except Exception as e:

        print(
            "TTS error:",
            e
        )


def main():

    print("=" * 50)
    print("        AIRA AI ASSISTANT")
    print("=" * 50)

    print("Aira is ready!")
    print("Speak naturally. Say 'exit' or 'bye' to stop.")

    print("=" * 50)


    conversation_history = []


    while True:

        text, info = listen()


        if not text:

            print(
                "I didn't understand you."
            )

            continue


        if is_exit_command(text):

            goodbye = "Okay, talk to you later!"

            print(
                "\nAssistant:",
                goodbye
            )

            speak_response(
                goodbye,
                info.language
            )

            break


        response = generate_response(
            text,
            conversation_history
        )


        if not response:

            continue


        print(
            "\nAssistant:",
            response
        )


        save_conversation(
            conversation_history,
            text,
            response
        )


        speak_response(
            response,
            info.language
        )


if __name__ == "__main__":

    main()