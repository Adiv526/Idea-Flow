from llm import call_llm
from problem import problem_prompt
from parser import parse_json

def run_problem_chain(idea):
    prompt = problem_prompt(idea)
    response = call_llm(prompt)
    return parse_json(response)
