from dotenv import load_dotenv
import os
from agents import (
    Agent,
    Runner,
    RunConfig,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    set_tracing_disabled,
    set_default_openai_client,
)

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError(
        "API key not found. Please set the OPENROUTER_API_KEY environment variable."
    )
BASE_URL = os.getenv("OPENROUTER_API_URL")
if not BASE_URL:
    raise ValueError(
        "Base URL not found. Please set the OPENROUTER_API_URL environment variable."
    )
gemini_model = os.getenv("OPENROUTER_GEMINI_MODEL")
if not gemini_model:
    raise ValueError(
        "Gemini model not found. Please set the OPENROUTER_GEMINI_MODEL environment variable."
    )
deepseek_model = os.getenv("OPENROUTER_DEEPSEEK_MODEL")
if not deepseek_model:
    raise ValueError(
        "Deepseek model not found. Please set the OPENROUTER_DEEPSEEK_MODEL environment variable."
    )


external_client = AsyncOpenAI(
    api_key=api_key,
    base_url=BASE_URL,
)
set_default_openai_client(external_client)
set_tracing_disabled(True)

model_gemini = OpenAIChatCompletionsModel(
    model=gemini_model,
    openai_client=external_client,
)
model_deepSeek = OpenAIChatCompletionsModel(
    model=deepseek_model,
    openai_client=external_client,
)


def agent_gemini():
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant.",
        model=model_gemini,
    )
    result = Runner.run_sync(
        agent, "Can we travell back in time, respond in a couple of lines?"
    )
    print("\n")
    print(result.final_output)
    print("\n")
    
    

def agent_deepseek():
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant.",
        model=model_deepSeek,
    )
    result = Runner.run_sync(
        agent, "What is butterfly effect, respond in a couple of lines?"
    )
    print("\n")
    print(result.final_output)
    print("\n")
