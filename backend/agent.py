import os
import re
from langchain_openai import ChatOpenAI
from weather_tool import get_weather

def run_agent(user_query: str):
    city = re.sub(r"[^a-zA-Z ]", "", user_query).split()[-1]
    weather = get_weather(city)

    # 🔒 SAFETY CHECK
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        return "OpenRouter API key not found"

    llm = ChatOpenAI(
        model="openai/gpt-3.5-turbo",  
        openai_api_key=api_key,
        base_url="https://openrouter.ai/api/v1",
        timeout=20,                   
    )

    try:
        response = llm.invoke(
            f"User asked: {user_query}. Weather info: {weather}. Respond simply."
        )
        return response.content
    except Exception as e:
        return f"LLM error: {str(e)}"
