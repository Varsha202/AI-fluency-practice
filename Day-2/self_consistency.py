import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def run_multiple():
    for i in range(5):
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[{"role": "user", "content": "Solve step by step: 200 + 300 + 400"}],
            temperature=0.7
        )

        print(f"\nRun {i+1}:")
        print(response.choices[0].message.content)

run_multiple()