from llm import get_llm
from problem_prompt import problem_prompt
from parser import parse_json

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


def run_problem_chain(idea):
    prompt = PromptTemplate(
        input_variables=["idea"],
        template=problem_prompt()
    )

    chain = LLMChain(
        llm=get_llm(),
        prompt=prompt
    )

    response = chain.invoke({"idea": idea})
    return parse_json(response["text"])
