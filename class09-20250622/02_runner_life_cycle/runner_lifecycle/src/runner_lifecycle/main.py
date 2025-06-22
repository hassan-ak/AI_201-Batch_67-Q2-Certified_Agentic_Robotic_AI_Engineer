from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    set_default_openai_api,
    set_default_openai_client,
    set_tracing_disabled,
    function_tool,
)
from runner_lifecycle.my_secrets import Secrets
from rich import print
from rich.panel import Panel
from rich.markdown import Markdown
from dataclasses import dataclass
from runner_lifecycle.runner_hooks import ExampleRunnerHooks
import random


@dataclass
class UserInfo:
    name: str


secrets = Secrets()

external_client = AsyncOpenAI(
    api_key=secrets.gemini_api_key, base_url=secrets.gemini_api_url
)
set_default_openai_client(external_client)
set_default_openai_api("chat_completions")
set_tracing_disabled(True)

user_info = UserInfo(name="John Doe")
runner_hooks = ExampleRunnerHooks()


@function_tool("random_number")
def random_number(max: int) -> int:
    """Generate a random number up to the provided max."""
    return random.randint(0, max)


@function_tool("multiply_by_two")
def multiply_by_two(x: int) -> int:
    """Return x times two."""
    return x * 2


multiply_agent = Agent(
    name="Multiply Agent",
    instructions="Multiply the number received during handoff by 2 and then return the final result.",
    tools=[multiply_by_two],
    model=secrets.gemini_api_model,
)

agent = Agent[UserInfo](
    name="Assistant",
    instructions="Generate a random number. If it's even, stop. If it's odd, hand off to the Multiply agent.",
    handoffs=[multiply_agent],
    model=secrets.gemini_api_model,
    tools=[random_number],
)


def main() -> None:
    user_input = input("Enter a max number: ")
    result = Runner.run_sync(
        starting_agent=agent,
        input=f"Generate a random number between 0 and {user_input}.",
        context=user_info,
        hooks=runner_hooks,
    )
    # Create a styled panel with the result
    markdown_content = Markdown(result.final_output)
    panel = Panel(
        markdown_content,
        title="[bold green]Assistant Response[/bold green]",
        border_style="blue",
        padding=(1, 2),
    )
    print(panel)
