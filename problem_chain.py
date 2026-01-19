from langchain.prompts import PromptTemplate
from llm import get_llm
from problem import problem_prompt
from parser import parse_json


def run_problem_chain(idea: str):
    llm = get_llm()

    prompt = PromptTemplate(
        template=problem_prompt(),
        input_variables=["idea"]
    )

    chain = prompt | llm

    response = chain.invoke({"idea": idea})

    return parse_json(response)
