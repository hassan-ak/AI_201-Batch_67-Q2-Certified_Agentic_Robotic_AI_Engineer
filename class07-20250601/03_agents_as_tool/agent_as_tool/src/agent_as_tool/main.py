from agents import (
    Agent,
    Runner,
    set_default_openai_client,
    AsyncOpenAI,
    set_tracing_disabled,
    set_default_openai_api,
)
from agent_as_tool.my_secrets import MySecrets
from rich import print

secrets = MySecrets()

external_client = AsyncOpenAI(
    api_key=secrets.gemini_api_key,
    base_url=secrets.gemini_api_url,
)

set_default_openai_client(external_client)
set_tracing_disabled(True)
set_default_openai_api("chat_completions")

spanish_agent = Agent(
    name="spanish_agent",
    instructions="You translate the user's message to Spanish.",
    model=secrets.gemini_api_model,
)

french_agent = Agent(
    name="french_agent",
    instructions="You translate the user's message to French.",
    model=secrets.gemini_api_model,
)

italian_agent = Agent(
    name="italian_agent",
    instructions="You translate the user's message to Italian.",
    model=secrets.gemini_api_model,
)

# triage Agent
triage_agent = Agent(
    name="triage_agent",
    instructions=(
        "You are a translation agent. You use the tools given to you to translate."
        "If asked for multiple translations, you call the relevant tools in order."
        "You never translate on your own, you always use the provided tools. Also mention which tool you used for translation."
    ),
    tools=[
        spanish_agent.as_tool(
            tool_name="translate_to_spanish",
            tool_description="Translate the user's message to Spanish",
        ),
        french_agent.as_tool(
            tool_name="translate_to_french",
            tool_description="Translate the user's message to French",
        ),
        italian_agent.as_tool(
            tool_name="translate_to_italian",
            tool_description="Translate the user's message to Italian",
        ),
    ],
    model=secrets.gemini_api_model,
)


def main():

    result = Runner.run_sync(triage_agent, "Translate 'Hello, how are you?' to Spanish, French and Italian.")

    print("\n")
    print(result.final_output)
