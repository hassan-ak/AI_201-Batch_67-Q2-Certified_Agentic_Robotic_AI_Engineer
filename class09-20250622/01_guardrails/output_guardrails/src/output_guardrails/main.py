from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    set_default_openai_api,
    set_default_openai_client,
    set_tracing_disabled,
    output_guardrail,
    RunContextWrapper,
    GuardrailFunctionOutput,
    OutputGuardrailTripwireTriggered
)
from rich import print
from rich.panel import Panel
from rich.markdown import Markdown
from dataclasses import dataclass
from output_guardrails.my_secrets import Secrets
from pydantic import BaseModel

secrets = Secrets()

external_client = AsyncOpenAI(
    api_key=secrets.gemini_api_key, base_url=secrets.gemini_api_url
)
set_default_openai_client(external_client)
set_default_openai_api("chat_completions")
set_tracing_disabled(True)


class MessageOutput(BaseModel):
    response: str


class MathOutput(BaseModel):
    is_math: bool
    reasoning: str


guardrail_agent2 = Agent(
    name="Guardrail check",
    instructions="Check if the output includes any math.",
    output_type=MathOutput,
    model=secrets.gemini_api_model,
)


@output_guardrail
async def math_guardrail2(
    ctx: RunContextWrapper, agent: Agent, output: MessageOutput
) -> GuardrailFunctionOutput:
    result = await Runner.run(guardrail_agent2, output, context=ctx.context)

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_math,
    )


agent = Agent(
    name="Customer support agent",
    instructions="You are a customer support agent. You help customers with their questions.",
    output_guardrails=[math_guardrail2],
    model=secrets.gemini_api_model,
)

def tripped() -> None:
    try:
        result = Runner.run_sync(
            agent, "Hello, can you help me solve for x: 2x + 3 = 11?"
        )
        print("Guardrail didn't trip - this is unexpected")
        print(result.final_output)
    except OutputGuardrailTripwireTriggered:
        print("Math output guardrail tripped")


def not_tripped() -> None:
    try:
        result = Runner.run_sync(agent, "Hello, can you help me with my order?")
        print("Guardrail didn't trip - this is expected")
        print(result.final_output)
    except OutputGuardrailTripwireTriggered:
        print("Math output guardrail tripped unexpectedly")
