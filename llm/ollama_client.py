import requests


URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2:3b"


SYSTEM_PROMPT = """
You are Aira, a personal AI voice assistant.

Your job is to understand the user's spoken request and respond naturally.

Important rules:

1. The user's input comes from speech-to-text and may contain small
   transcription errors, especially in Hindi and Hinglish.
2. Infer the user's intended meaning from context when the mistake is obvious.
3. Do not mention or explain speech-to-text errors unless the user asks.
4. Support English, Hindi, and Hinglish naturally.
5. Reply in the same language or style as the user whenever possible.
6. Keep responses concise and conversational because your response will be
   spoken aloud using text-to-speech.
7. Avoid unnecessary headings, bullet points, markdown, tables, and long
   explanations unless the user explicitly asks for a detailed explanation.
8. Never pretend to have performed an action if you have not actually
   performed it.
9. If the user's request is unclear, ask a short clarification question.
10. Be helpful, natural, and conversational.
11. Remember the previous conversation and use it when answering follow-up
    questions.
12. Do not repeat information unnecessarily.

You are running locally as part of a personal AI assistant.
"""


def ask(prompt, conversation_history=None):

    if conversation_history is None:
        conversation_history = []

    # --------------------------------------------------
    # Build messages
    # --------------------------------------------------

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    # Add previous conversation
    messages.extend(conversation_history)

    # Add current user message
    messages.append({
        "role": "user",
        "content": prompt
    })

    # --------------------------------------------------
    # Send request to Ollama
    # --------------------------------------------------

    response = requests.post(
        URL,
        json={
            "model": MODEL,
            "messages": messages,
            "stream": False
        },
        timeout=120
    )

    response.raise_for_status()

    data = response.json()

    return data["message"]["content"].strip()