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
ACCESS_TOKEN=your_token_here  

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
cd <your-repo>  

python -m venv venv  
source venv/bin/activate  

pip install -r requirements.txt  
python manage.py migrate  
python manage.py runserver  

---

## 📄 License

MIT License

Copyright (c) 2025  
Washifur Rahman
