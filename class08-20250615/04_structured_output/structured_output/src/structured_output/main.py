from agents import (
    Agent,
    Runner,
    OpenAIChatCompletionsModel,
    set_tracing_disabled,
    set_default_openai_client,
    set_default_openai_api,
    AsyncOpenAI,
    function_tool,
    AgentOutputSchemaBase
)
from structured_output.my_secrets import Secrets
from rich import print
from dataclasses import dataclass

secrets = Secrets()

external_client = AsyncOpenAI(
    base_url=secrets.gemini_api_url,
    api_key=secrets.gemini_api_key,
)

set_default_openai_client(external_client)
set_tracing_disabled(True)
set_default_openai_api("chat_completions")

@dataclass
class Weather_Output:
    location: str
    temperature: float
    condition: str
    summary: str

agent = Agent(
    name="Assistant",
    instructions= "You are a helpful weather assistant. Provide accurate weather information.",
    model = secrets.gemini_api_model,
    output_type=Weather_Output,
)

def main_structured():
    result = Runner.run_sync(
        starting_agent=agent,
        input="What is the weather in New York?",
    )
    
    print(result.final_output)
