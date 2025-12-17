# 🤖 Chatbot API

A simple REST API for user authentication and chatbot interaction.  
Designed for web and mobile clients that require conversational AI features.

---

## 📌 Base URL (Local Development)

http://127.0.0.1:8000

---

## 📚 Table of Contents

- Overview  
- Authentication  
- API Endpoints  
- Using with Postman  
- Environment Variables  
- Error Handling  
- Development  
- License  

---

## 🧩 Overview

The Chatbot API provides:

- User registration (signup)
- User authentication (JWT / token-based)
- Sending messages to a chatbot
- Fetching previous chat history for authenticated users

---

## 🔐 Authentication

All protected endpoints require **Bearer Token Authentication**.

Authorization header format:

Authorization: Bearer <your_token_here>

---

## 🚀 API Endpoints

### POST /api/users/signup/

Register a new user.

Request body:
{
  "email": "user@example.com",
  "username": "example_user",
  "password": "StrongPassword123!",
  "password_confirm": "StrongPassword123!"
}

---

### POST /api/users/login/

Authenticate a user and receive an access token.

Request body:
{
  "email": "user@example.com",
  "password": "StrongPassword123!"
}

---

### POST /api/chat/

Send a message to the chatbot.  
Requires authentication.

Request body:
{
  "message": "Hello, how are you?"
}

---

### GET /api/chat-history/

Fetch previous chat history.  
Requires authentication.

---

## 🧪 Using with Postman

Recommended steps:

1. Signup
2. Login
3. Copy access token
4. Set Authorization header:
   Authorization: Bearer <token>
5. Call chat and chat-history endpoints

---

## 🌱 Environment Variables

BASE_URL=http://127.0.0.1:8000  
OPENAI_API_KEY=your_key_here

---

## ⚠️ Error Handling

Common status codes:

- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found
- 500 Internal Server Error

---

## 🛠 Development

Example setup (Django):

git clone https://github.com/<your-username>/<your-repo>.git  
cd <your-repo>  [Uploading README (1).md…]()


python -m venv venv  
source venv/bin/activate  

pip install -r requirements.txt  
python manage.py migrate  
python manage.py runserver  

---

## FAQs and Summary


# Backend-Only AI Chatbot with RAG Pipeline (Django REST Framework)

## 📌 Project Overview

This project is a **backend-only AI chatbot service** built using **Django REST Framework**.  
It supports:

- User authentication using **JWT**
- Secure chat endpoints
- Persistent **chat history storage**
- AI-generated responses using **OpenAI GPT**
- A **Retrieval-Augmented Generation (RAG) pipeline** structure
- Background tasks for housekeeping (e.g., deleting old chat history)

The system is designed to be **scalable, secure, and production-ready**, focusing entirely on backend functionality.

---

## 🛠 Technologies Used

- **Python 3**
- **Django & Django REST Framework**
- **SQLite** (development database)
- **JWT Authentication** (`djangorestframework-simplejwt`)
- **OpenAI API (GPT-3.5-turbo)**
- **APScheduler** (background tasks)
- **Postman** (API testing)

---

## 🔐 Authentication (JWT)

### How authentication was implemented

- User registration (`/signup`) creates a user with a **hashed password**
- Login (`/login`) returns a **JWT access token**
- All protected endpoints require:

```
Authorization: Bearer <ACCESS_TOKEN>
```

### Security Measures

- Passwords are hashed using Django’s built-in password hashing
- JWT tokens have expiration times
- Tokens are validated on every request
- Authentication middleware blocks unauthorized access

---

## 💾 Database & Model Design

### Database Used

- **SQLite** (chosen for simplicity and fast local development)
- Easily replaceable with PostgreSQL for production

### Models

#### ChatMessage Model

```python
class ChatMessage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_message = models.TextField()
    bot_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

### Why this structure?

- Each chat message is linked to a specific user
- Supports efficient filtering by user
- Enables easy retrieval of chat history
- Simple and scalable schema

---

## 🤖 RAG Pipeline Integration

### How the RAG pipeline works

1. User sends a message to `/chat`
2. Relevant documents (future extension) can be retrieved from a knowledge base
3. Retrieved context is combined with the user query
4. The AI model generates a response using both context and language understanding

Currently, direct AI generation is used while keeping the RAG structure extensible.

---

## 🧠 AI Response Generation

The chatbot uses **OpenAI GPT-3.5-turbo**.

```python
def rag_pipeline(query):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": query}],
        max_tokens=150,
        temperature=0.7,
    )
    return response.choices[0].message.content
```

---

## 📜 Chat History

### Endpoint

```
GET /api/chat-history/
```

- JWT protected
- Returns user-specific chat history
- Ordered by timestamp

---

## ⏰ Background Tasks

- Background cleanup task deletes chat history older than **30 days**
- Implemented using **APScheduler**
- Runs daily to keep the database optimized

---

## 🧪 Testing Strategy

- Manual API testing using **Postman**
- Authentication testing with valid/invalid JWTs
- Error handling and edge case testing
- Logging for debugging external API failures

---

## 🔗 External Services Integrated

| Service | Purpose |
|------|--------|
| OpenAI API | AI text generation |
| JWT | Secure authentication |
| APScheduler | Background task scheduling |

---

## 🚀 Future Improvements

- Vector search using FAISS or Pinecone
- Real-time knowledge base updates
- Multi-user chat rooms
- WebSocket-based real-time chat
- Rate limiting and analytics

---

## ⚙️ Setup Instructions

```bash
git clone <repo_url>
cd ai_chatbot_backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Environment Variables

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

## 📬 API Endpoints Summary

| Method | Endpoint | Description |
|------|---------|------------|
| POST | /api/users/signup | Register user |
| POST | /api/users/login | Login & receive JWT |
| POST | /api/chat | Send message to chatbot |
| GET | /api/chat-history | Retrieve chat history |

---

## ✅ Conclusion

This project demonstrates a secure and scalable backend chatbot architecture using Django REST Framework, JWT authentication, and OpenAI integration. It is production-ready and easily extensible.



## 📄 License

MIT License

Copyright (c) 2025  
Washifur Rahman
