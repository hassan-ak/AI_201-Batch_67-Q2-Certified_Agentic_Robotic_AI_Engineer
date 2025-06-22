from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    set_default_openai_api,
    set_default_openai_client,
    set_tracing_disabled,
    input_guardrail,
    RunContextWrapper,
    TResponseInputItem,
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered
)
from rich import print
from rich.panel import Panel
from rich.markdown import Markdown
from dataclasses import dataclass
from input_guardrails.my_secrets import Secrets
from pydantic import BaseModel

secrets = Secrets()

external_client = AsyncOpenAI(
    api_key=secrets.gemini_api_key, base_url=secrets.gemini_api_url
)
set_default_openai_client(external_client)
set_default_openai_api("chat_completions")
set_tracing_disabled(True)

class MathHomeworkOutput(BaseModel):
    is_math_homework: bool
    reasoning: str

guardrail_agent = Agent(
    name="Guardrail check",
    instructions="Check if the user is asking you to do their math homework.",
    output_type=MathHomeworkOutput,
    model=secrets.gemini_api_model,
)


@input_guardrail
async def math_guardrail(
    ctx: RunContextWrapper[None], agent: Agent, input: str | list[TResponseInputItem]
) -> GuardrailFunctionOutput:
    result = await Runner.run(guardrail_agent, input, context=ctx.context)

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        # tripwire_triggered=False #result.final_output.is_math_homework,
        tripwire_triggered=result.final_output.is_math_homework,
    )

agent = Agent(
    name="Customer support agent",
    instructions="You are a customer support agent. You help customers with their questions.",
    input_guardrails=[math_guardrail],
    model=secrets.gemini_api_model,
)


def tripped() -> None:
    try:
        result = Runner.run_sync(agent, "Hello, can you help me solve for x: 2x + 3 = 11?")
        print("Guardrail didn't trip - this is unexpected")
        print(result.final_output)
    except InputGuardrailTripwireTriggered:
        print("Math homework guardrail tripped")

def not_tripped() -> None:
    try:
        result = Runner.run_sync(agent, "Hello, can you help me with my order?")
        print("Guardrail didn't trip - this is expected")
        print(result.final_output)
    except InputGuardrailTripwireTriggered:
        print("Math homework guardrail tripped unexpectedly")