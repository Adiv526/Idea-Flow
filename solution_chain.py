from llm import get_llm
from solution import solution_prompt
from parser import parse_json

def run_solution_chain(idea):
    prompt = problem_prompt(idea)
    response = call_llm(prompt)
    return parse_json(response)
