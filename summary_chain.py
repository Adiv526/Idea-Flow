from llm import call_llm
from risk import risk_prompt
from parser import parse_json

def run_summary_chain(idea, problem, customer, market, solution, risk):
    prompt = PromptTemplate(
        input_variables=[
            "idea", "problem", "customer",
            "market", "solution", "risk"
        ],
        template=summary_prompt()
    )

   
    response = chain.invoke({
    "idea": idea,
    "problem": problem,
    "customer": customer,
    "market": market,
    "solution": solution,
    "risk": risk
})
    return parse_json(response)

