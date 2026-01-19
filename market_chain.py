
from llm import call_llm
from market import market_prompt
from parser import parse_json


def run_market_chain(idea):
    prompt = problem_prompt(idea)
    response = call_llm(prompt)
    return parse_json(response)
