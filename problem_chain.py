from langchain import LLMChain
from models.llm import get_llm
from prompts.problem import problem_prompt
from utils.parser import parse_json
from langchain.prompts import PromptTemplate

def run_problem_chain(idea):
    prompt = PromptTemplate(
        input_variables=["idea"],
        template=problem_prompt()
    )

    chain = LLMChain(llm=get_llm(), prompt=prompt)
    result = chain.run(idea=idea)

    return parse_json(result)
