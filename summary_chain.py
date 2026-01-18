from langchain import LLMChain
from models.llm import get_llm
from prompts.summary import summary_prompt
from utils.parser import parse_json
from langchain.prompts import PromptTemplate

def run_summary_chain(idea, problem, customer, market, solution, risk):
    prompt = PromptTemplate(
        input_variables=[
            "idea", "problem", "customer",
            "market", "solution", "risk"
        ],
        template=summary_prompt()
    )

    chain = LLMChain(llm=get_llm(), prompt=prompt)
    result = chain.run(
        idea=idea,
        problem=problem,
        customer=customer,
        market=market,
        solution=solution,
        risk=risk
    )

    return parse_json(result)
