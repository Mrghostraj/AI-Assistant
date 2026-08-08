from speech.recorder import record
from speech.transcriber import transcribe
from speech.speaker import speak

from llm.ollama_client import ask

while True:

    input("Press ENTER to speak...")

    audio = record()

    text = transcribe(audio)

    print("\nYou:", text)

    if text.lower() in ["exit", "quit", "bye"]:

        break

    reply = ask(text)

    print("\nJarvis:", reply)

    speak(reply)