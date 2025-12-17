from .retriever import retrieve_docs
from .generator import generate_answer

# def rag_pipeline(query):
#     docs = retrieve_docs(query)
#     if docs:
#         return generate_answer(query, docs)
#     return generate_answer(query, [])

import openai, os

openai.api_key = os.getenv("OPENAI_API_KEY")

def rag_pipeline(query):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": query}],
            max_tokens=150,
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        import traceback
        traceback.print_exc()
        return f"OpenAI error: {str(e)}"
