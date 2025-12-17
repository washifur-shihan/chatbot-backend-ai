def retrieve_docs(query):
    docs = [
        "JWT is used for authentication",
        "Django REST Framework supports JWT"
    ]
    return docs if "jwt" in query.lower() else []
