from pydantic import BaseModel
from agents import Agent, GuardrailFunctionOutput, RunContextWrapper, Runner, output_guardrail
from my_secrets import Secrets

secrets = Secrets()

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
async def math_output_guardrail(
    ctx: RunContextWrapper, agent: Agent, output: MessageOutput
) -> GuardrailFunctionOutput:
    print(f"Output: Guardrail triggered", output)
    result = await Runner.run(guardrail_agent2, output, context=ctx.context)

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_math,
    )