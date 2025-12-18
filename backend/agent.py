import os
from langchain_openai import ChatOpenAI
from weather_tool import get_weather

def run_agent(user_query: str):

    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        openai_api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1"
    )

    city = user_query.split()[-1]
    weather = get_weather(city)

    prompt = f"""
    User question: {user_query}
    Weather info: {weather}
    Respond clearly.
    """

    response = llm.invoke(prompt)
    return response.content
