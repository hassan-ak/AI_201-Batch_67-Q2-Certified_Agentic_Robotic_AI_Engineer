import chainlit as cl
from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    set_default_openai_api,
    set_default_openai_client,
    set_tracing_disabled,
    function_tool,
)
from my_secrets import Secrets
from typing import cast, List
import json
from rich import print
from openai.types.responses import ResponseTextDeltaEvent
import requests

secrets = Secrets()


@cl.set_starters
async def set_starts() -> List[cl.Starter]:
    return [
        cl.Starter(
            label="Essay Writing",
            message="Write an essay on the impact of technology on education.",
        ),
        cl.Starter(
            label="Weather",
            message="Find the weather in Karachi.",
        ),
    ]


@function_tool("current_weather_tool")
@cl.step(type="weather tool")
def current_weather_tool(location: str) -> str:
    """
    This function makes a request to a weather API and returns formatted weather
    information including temperature, conditions, wind, humidity, and UV index.

    Args:
        location (str): The location to get weather for (city name)

    Returns:
        str: A formatted string containing current weather information if successful,
             or an error message if the API request fails
    """
    result = requests.get(
        f"{secrets.weather_api_url}/current.json?key={secrets.weather_api_key}&q={location}"
    )
    if result.status_code == 200:
        data = result.json()
        return f"Current weather in {data['location']['name']}, {data['location']['region']}, {data['location']['country']} as of {data['location']['localtime']} is {data['current']['temp_c']}°C ({data['current']['condition']['text']}), feels like {data['current']['feelslike_c']}°C, wind {data['current']['wind_kph']} km/h {data['current']['wind_dir']}, humidity {data['current']['humidity']}% and UV index is {data['current']['uv']}."
    else:
        return "Sorry, I couldn't fetch the weather data. Please try again later"


@cl.on_chat_start
def on_chat_start():
    external_client = AsyncOpenAI(
        api_key=secrets.gemini_api_key,
        base_url=secrets.gemini_api_url,
    )
    set_default_openai_client(external_client)
    set_tracing_disabled(True)
    set_default_openai_api("chat_completions")

    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant. Whihc can help users with their queries and can use tools to get answers.",
        model=secrets.gemini_api_model,
        tools=[current_weather_tool],
    )
    cl.user_session.set("agent", agent)
    cl.user_session.set("chat_history", [])


@cl.on_message
async def handle_message(msg: cl.Message):
    message = cl.Message(content="")
    agent = cast(Agent, cl.user_session.get("agent"))
    chat_history: list = cl.user_session.get("chat_history") or []
    chat_history.append({"role": "user", "content": msg.content})
    try:
        result = Runner.run_streamed(
            starting_agent=agent,
            input=chat_history,
        )
        async for event in result.stream_events():
            if event.type == "raw_response_event" and isinstance(
                event.data, ResponseTextDeltaEvent
            ):
                await message.stream_token(event.data.delta)
        await message.update()
    except Exception as e:
        await message.send(f"Unable to process your request, Please try again later.")


@cl.on_chat_end
def on_chat_end():
    chat_history = cl.user_session.get("chat_history") or []
    with open("chat_history.json", "w") as f:
        json.dump(chat_history, f, indent=2)
