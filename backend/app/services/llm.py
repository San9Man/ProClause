import requests
from app.config import OPENROUTER_API_KEY

def call_llm(prompt):
    try:
        print("🔵 Sending request to OpenRouter...")

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "http://localhost",
                "X-Title": "Legal AI Agent"
            },
            json={
                "model": "meta-llama/llama-3-8b-instruct",
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            },
            timeout=30
        )

        print("🟢 STATUS CODE:", response.status_code)
        print("🟡 RESPONSE TEXT:", response.text)

        if response.status_code != 200:
            return "AI request failed"

        data = response.json()
        return data["choices"][0]["message"]["content"]

    except Exception as e:
        print("🔴 ERROR:", str(e))
        return "AI request failed"