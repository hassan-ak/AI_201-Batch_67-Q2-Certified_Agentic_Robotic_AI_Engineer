from agents import (
    Agent,
    Runner,
    set_tracing_disabled,
    set_default_openai_client,
    set_default_openai_api,
    AsyncOpenAI,
    function_tool,
)
from weather_agnet.my_secrets import Secrets
from rich import print
import requests

secrets = Secrets()

external_client = AsyncOpenAI(
    base_url=secrets.gemini_api_url,
    api_key=secrets.gemini_api_key,
)

set_default_openai_client(external_client)
set_tracing_disabled(True)
set_default_openai_api("chat_completions")


@function_tool("current_weather_tool")
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


agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant. You can answer questions and perform tasks using tools.",
    model=secrets.gemini_api_model,
    tools=[current_weather_tool],
)


def main():
    result = Runner.run_sync(
        starting_agent=agent,
        input="What is the weather in Faisalabad?",
    )

    print(result.final_output)
