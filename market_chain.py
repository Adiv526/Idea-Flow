from langchain import LLMChain
from llm import get_llm
from market import market_prompt
from parser import parse_json
from langchain.prompts import PromptTemplate

def run_market_chain(idea):
    prompt = PromptTemplate(
        input_variables=["idea"],
        template=market_prompt()
    )

    chain = LLMChain(llm=get_llm(), prompt=prompt)
    result = chain.run(idea=idea)

    return parse_json(result)
