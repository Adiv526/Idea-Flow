
from llm import call_llm
from customer import customer_prompt
from parser import parse_json


def run_customer_chain(idea):
    prompt = problem_prompt(idea)
    response = call_llm(prompt)
    return parse_json(response)
