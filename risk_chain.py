from langchain import LLMChain
from models.llm import get_llm
from prompts.risk import risk_prompt
from utils.parser import parse_json
from langchain.prompts import PromptTemplate

def run_risk_chain(idea):
    prompt = PromptTemplate(
        input_variables=["idea"],
        template=risk_prompt()
    )

    chain = LLMChain(llm=get_llm(), prompt=prompt)
    result = chain.run(idea=idea)

    return parse_json(result)
