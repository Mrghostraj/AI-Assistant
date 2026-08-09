import requests

URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5:3b"


def ask(prompt):

    response = requests.post(
        URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "system": (
                "You are a voice assistant."
                "Give Concise Natural Spoken responses."
                "Do not use Markdown, bullet points, or headings. "
                "Keep responses under 3 sentences unless more detail is requested."
            ),
            "stream": False
        },
        timeout=120
    )

    response.raise_for_status()

    return response.json()["response"]