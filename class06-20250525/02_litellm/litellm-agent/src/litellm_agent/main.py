from litellm_agent.secerts import Secrets
from agents import Agent, Runner, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
from rich import print

secrets = Secrets()
set_tracing_disabled(True)


def run_gemini():
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant.",
        model=LitellmModel(
            api_key=secrets.gemini_api_key,
            model=secrets.gemini_model,
        ),
    )
    result = Runner.run_sync(agent, "What is AI? Respond in a single line.")
    print(result.final_output)


def run_groq():
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant.",
        model=LitellmModel(
            api_key=secrets.groq_api_key,
            model=secrets.groq_model,
        ),
    )
    result = Runner.run_sync(agent, "What is GenAI? Respond in a single line.")
    print(result.final_output)
