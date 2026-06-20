import requests
import json

# Replace with your Gemini API key
API_KEY = "AQ.Ab8RN6I29ar_LnpHYwegd0lyUXwKjLbfy22DbuE07GeKjKK8Tg"

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

question = input("Ask Gemini: ")

payload = {
    "contents": [
        {
            "parts": [
                {
                    "text": question
                }
            ]
        }
    ]
}

response = requests.post(
    url,
    headers={"Content-Type": "application/json"},
    data=json.dumps(payload)
)

response.raise_for_status()

result = response.json()

try:
    answer = result["candidates"][0]["content"]["parts"][0]["text"]
    print("\nGemini:")
    print(answer)
except (KeyError, IndexError):
    print("Unexpected response:")
    print(json.dumps(result, indent=2))