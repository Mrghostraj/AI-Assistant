import requests

URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5:3b"


def ask(prompt):

    response = requests.post(
        URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )

    response.raise_for_status()

    return response.json()["response"]