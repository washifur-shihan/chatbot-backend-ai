import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_answer(query, docs):
    context = "\n".join(docs)
    prompt = f"Context: {context}\nQuestion: {query}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
