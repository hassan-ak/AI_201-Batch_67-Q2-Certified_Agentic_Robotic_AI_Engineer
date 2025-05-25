from agents import (
    Agent,
    Runner,
    OpenAIChatCompletionsModel,
    set_tracing_disabled,
    set_default_openai_client,
    set_default_openai_api,
    AsyncOpenAI,
    function_tool
)
from agent_with_tools.my_secrets import Secrets
from rich import print

secrets = Secrets()

external_client = AsyncOpenAI(
    base_url=secrets.gemini_api_url,
    api_key=secrets.gemini_api_key,
)

set_default_openai_client(external_client)
set_tracing_disabled(True)
set_default_openai_api("chat_completions")

@function_tool("weather_tool")
def weather_tool(location: str) -> str:
    """
    Get the current weather for a given location.
    """
    # Simulate a weather API call
    return f"The current weather in {location} is sunny with a temperature of 25°C."

@function_tool("student_finder_tool")
def student_finder_tool(roll_number: int) -> str:
    """
    Find a student by roll number.
    """
    data = {
        101: "Alice Smith",
        102: "Bob Johnson",
        103: "Charlie Brown"
    }
    student_name = data.get(roll_number, "Student not found.")
    return f"The student with roll number {roll_number} is {student_name}."
    

agent = Agent(
    name="Assistant",
    instructions= "You are a helpful assistant. You can answer questions and perform tasks using tools.",
    model = secrets.gemini_api_model,
    tools=[
        weather_tool,
        student_finder_tool
    ],
)

def main():
    result = Runner.run_sync(
        starting_agent=agent,
        input="Which student have roll number 102? Also, what is the weather in New York?",
    )
    
    print(result.final_output)

