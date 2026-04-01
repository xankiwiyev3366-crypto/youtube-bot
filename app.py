import os
import requests

API_KEY = os.getenv("ANTHROPIC_API_KEY")

def get_ideas(topic):
    url = "https://api.anthropic.com/v1/messages"

    headers = {
        "x-api-key": API_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }

    prompt = f"""
    Give me 10 viral YouTube Shorts ideas about {topic}.
    Each idea must include:
    - Title
    - Hook
    - Short description
    """

    data = {
        "model": "claude-3-haiku-20240307",
        "max_tokens": 500,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    print(response.json())

if __name__ == "__main__":
    get_ideas("luxury cars")
