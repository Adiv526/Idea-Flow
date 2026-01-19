from llm import call_llm
from summary import summary_prompt
from parser import parse_json

def run_summary_chain(idea, problem, customer, market, solution, risk):
    prompt = summary_prompt(
        idea, problem, customer, market, solution, risk
    )
    response = call_llm(prompt)
    return parse_json(response)
