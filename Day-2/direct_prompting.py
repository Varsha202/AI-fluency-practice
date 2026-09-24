import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask(question):
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": question}],
        temperature=0
    )
    return response.choices[0].message.content

print(ask("How much did I spend on Food in June 2025?"))