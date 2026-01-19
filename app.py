import streamlit as st

from problem_chain import run_problem_chain
from customer_chain import run_customer_chain
from market_chain import run_market_chain
from solution_chain import run_solution_chain
from risk_chain import run_risk_chain
from summary_chain import run_summary_chain

st.title("🚀 AI Idea Validator")

idea = st.text_area("Describe your startup idea")

if st.button("Validate") and idea.strip():

    with st.spinner("Analyzing your idea like a VC..."):
        prompt = full_validation_prompt(idea)
        response = call_llm(prompt)
        result = parse_json(response)

        """
        problem = run_problem_chain(idea)
        customer = run_customer_chain(idea)
        market = run_market_chain(idea)
        solution = run_solution_chain(idea)
        risk = run_risk_chain(idea)
        summary = run_summary_chain(
            idea, problem, customer, market, solution, risk
        )"""

    st.tabs(["Problem","Customer","Market","Solution","Risks","Summary"])

    st.json(result["problem"])
    st.json(result["customer"])
    st.json(result["market"])
    st.json(result["solution"])
    st.json(result["risk"])
    st.json(result["summary"])
