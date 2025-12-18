# llm-weather-assistant
LLM-powered weather assistant using React, FastAPI, LangChain, and OpenRouter

# 🌤️ LLM-Powered Weather Assistant

A minimal full-stack web application that demonstrates how a Large Language Model (LLM) can dynamically use external tools to answer real-world queries.  
The application allows users to ask weather-related questions in natural language and receive real-time responses.

---

## 🚀 Project Overview

This project consists of a React-based frontend and a FastAPI-based backend.  
The backend integrates **LangChain** with an **LLM via OpenRouter**, enabling the system to understand user intent and decide when to call a weather tool.

Instead of using hard-coded rules, the LLM interprets natural language queries and invokes the appropriate tool to fetch live weather data.

---

## 🧠 Key Features

- 🌐 React frontend with a clean and simple UI  
- ⚡ FastAPI backend for handling API requests  
- 🤖 LLM integration using LangChain + OpenRouter  
- 🛠️ Tool-based reasoning to fetch real-time weather data  
- 🗣️ Supports natural language queries like:
  - *“What’s the weather of Pune?”*
  - *“Weather of Mumbai today”*
  - *“Is it hot in Delhi?”*
- ❌ Graceful handling of invalid city names and API failures  

---

## 🔄 Application Flow

User
↓
React Frontend
↓
FastAPI Backend
↓
LangChain Agent
↓
LLM (via OpenRouter)
↓
Weather Tool (API)
↓
Formatted Natural Language Response


---

## 🛠️ Technology Stack

### Frontend
- React (Vite)
- JavaScript
- HTML & CSS

### Backend
- FastAPI
- Python

### AI & Tools
- LangChain
- OpenRouter (LLM provider)
- OpenWeather API

---

## 🧩 Why Use an LLM?

- Handles natural language variations instead of keyword matching  
- Dynamically decides when a tool is required  
- Clean separation between reasoning and business logic  
- Easily extensible to additional tools (e.g., air quality, forecast)

---

## ⚠️ Error Handling

- Invalid city names are handled gracefully  
- External API failures do not crash the application  
- User-friendly error messages are returned  

---

## 📂 Project Structure

llm-weather-assistant/
├── backend/
│ ├── main.py
│ ├── agent.py
│ ├── weather_tool.py
│ └── .env (ignored)
├── frontend/
│ ├── src/
│ ├── package.json
│ └── node_modules (ignored)
├── .gitignore
└── README.md


---

## ▶️ How to Run the Project

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

Frontend-
cd frontend
npm install
npm run dev

Open the application at:
http://localhost:5173



🌱 Future Enhancements

Add more tools (air quality, humidity, forecast)

Improve UI styling and animations

Deploy the application to cloud platforms

📝 Summary

This project demonstrates how LLMs can be used beyond simple chat applications by enabling tool-based reasoning for real-world data access.
The focus is on clean architecture, reasoning transparency, and extensibility.