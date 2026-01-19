
from llm import call_llm
from risk import risk_prompt
from parser import parse_json


def run_risk_chain(idea):
    prompt = problem_prompt(idea)
    response = call_llm(prompt)
    return parse_json(response)
