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
    InputGuardrailTripwireTriggered,
    OutputGuardrail,
    OutputGuardrailTripwireTriggered,
)
from rich import print
from rich.panel import Panel
from rich.markdown import Markdown
from dataclasses import dataclass
from guardrails_combined.my_secrets import Secrets
from pydantic import BaseModel

secrets = Secrets()

external_client = AsyncOpenAI(
    api_key=secrets.gemini_api_key, base_url=secrets.gemini_api_url
)
set_default_openai_client(external_client)
set_default_openai_api("chat_completions")
set_tracing_disabled(True)


# Define the output model for the guardrail agents
class PIAICRelevanceOutput(BaseModel):
    is_piaic_relevant: bool
    reasoning: str


# Create the input guardrail agent to check if input is PIAIC-related
input_guardrail_agent = Agent(
    name="PIAIC_Input_Relevance_Check",
    instructions=(
        "You are a guardrail agent that checks if the user's input is related to PIAIC (Presidential Initiative for Artificial Intelligence and Computing) topics, "
        "such as Artificial Intelligence, Cloud Native Computing, Blockchain, Internet of Things (IoT), or other PIAIC courses. "
        "Determine if the input is relevant to PIAIC. "
        "Return a structured output with 'is_piaic_relevant' as a boolean and 'reasoning' explaining your decision."
    ),
    output_type=PIAICRelevanceOutput,
    model=secrets.gemini_api_model,
)

# Create the output guardrail agent to check if output is PIAIC-related
output_guardrail_agent = Agent(
    name="PIAIC_Output_Relevance_Check",
    instructions=(
        "You are a guardrail agent that checks if the agent's response is related to PIAIC (Presidential Initiative for Artificial Intelligence and Computing) topics, "
        "such as Artificial Intelligence, Cloud Native Computing, Blockchain, Internet of Things (IoT), or other PIAIC courses. "
        "Determine if the response content is relevant to PIAIC. "
        "Return a structured output with 'is_piaic_relevant' as a boolean and 'reasoning' explaining your decision."
    ),
    output_type=PIAICRelevanceOutput,
    model=secrets.gemini_api_model,
)


# Define the input guardrail function
@input_guardrail
async def piaic_input_relevance_guardrail(
    ctx: RunContextWrapper[None],
    agent: Agent,
    input: str | list,
) -> GuardrailFunctionOutput:
    result = await Runner.run(input_guardrail_agent, input, context=ctx.context)
    final_output = result.final_output_as(PIAICRelevanceOutput)
    return GuardrailFunctionOutput(
        output_info=final_output,
        tripwire_triggered=not final_output.is_piaic_relevant,
    )


# Define the output guardrail function
async def piaic_output_relevance_guardrail(
    ctx: RunContextWrapper[None],
    agent: Agent,
    output: str | list,
) -> GuardrailFunctionOutput:
    result = await Runner.run(output_guardrail_agent, output, context=ctx.context)
    final_output = result.final_output_as(PIAICRelevanceOutput)
    return GuardrailFunctionOutput(
        output_info=final_output,
        tripwire_triggered=not final_output.is_piaic_relevant,
    )


# Create the main PIAIC agent with both input and output guardrails
piaic_agent = Agent(
    name="PIAIC_Assistant",
    instructions=(
        "You are a helpful assistant for PIAIC-related questions. "
        "Answer questions about PIAIC courses, such as AI, Cloud Native Computing, Blockchain, IoT, or other PIAIC initiatives. "
        "Provide accurate and concise information."
    ),
    input_guardrails=[piaic_input_relevance_guardrail],
    output_guardrails=[
        OutputGuardrail(guardrail_function=piaic_output_relevance_guardrail)
    ],
    model=secrets.gemini_api_model,
)


def tripped() -> None:
    try:
        result = Runner.run_sync(piaic_agent, "How do I bake a chocolate cake?")
        print("Response:", result.final_output)
    except InputGuardrailTripwireTriggered as e:
        print("Input Guardrail tripped: Input is not PIAIC-related.")
    except OutputGuardrailTripwireTriggered as e:
        print("Output Guardrail tripped: Response is not PIAIC-related.")


def not_tripped() -> None:
    try:
        result = Runner.run_sync(
            piaic_agent,
            "What is genAI?",
        )
        print("Response:", result.final_output)
    except InputGuardrailTripwireTriggered as e:
        print("Input Guardrail tripped: Input is not PIAIC-related.")
    except OutputGuardrailTripwireTriggered as e:
        print("Output Guardrail tripped: Response is not PIAIC-related.")
