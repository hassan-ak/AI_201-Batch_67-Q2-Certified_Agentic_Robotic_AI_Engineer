from litellm_agent.secerts import gemini_api_key, gemini_model, groq_api_key, groq_model

from agents import Agent, Runner, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel

set_tracing_disabled(True)


def run_gemini():
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant.",
        model=LitellmModel(
            api_key=gemini_api_key,
            model=gemini_model,
        ),
    )
    result = Runner.run_sync(agent, "What is AI? Respond in a single line.")
    print(result.final_output)


def run_groq():
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant.",
        model=LitellmModel(
            api_key=groq_api_key,
            model=groq_model,
        ),
    )
    result = Runner.run_sync(agent, "What is GenAI? Respond in a single line.")
    print(result.final_output)
