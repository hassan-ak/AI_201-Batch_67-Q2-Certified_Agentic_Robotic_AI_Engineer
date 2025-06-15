from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    set_default_openai_api,
    set_default_openai_client,
    set_tracing_disabled,
)
from agent_with_handoffs.my_secrets import Secrets

secrets = Secrets()

external_client = AsyncOpenAI(
    api_key=secrets.gemini_api_key,
    base_url=secrets.gemini_api_url,
)

set_default_openai_client(external_client)
set_default_openai_api("chat_completions")
set_tracing_disabled(True)


urdu_agent = Agent(name="Urdu agent", instructions="You only speak Urdu.", model=secrets.gemini_api_model)

english_agent = Agent(name="English agent", instructions="You only speak English",  model=secrets.gemini_api_model)

triage_agent = Agent(
    name="Triage agent",
    instructions="Handoff to the appropriate agent based on the language of the request.",
    handoffs=[urdu_agent, english_agent],
    model=secrets.gemini_api_model
)


def main():
    result = Runner.run_sync(triage_agent, "السلام عليكم")
    result = Runner.run_sync(triage_agent, "Hello, how are you?")
    print(result.final_output)
