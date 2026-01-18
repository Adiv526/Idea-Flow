import streamlit as st

from chains.problem_chain import run_problem_chain
from chains.customer_chain import run_customer_chain
...

st.title("AI Idea Validator")

idea = st.text_area("Describe your idea")

if st.button("Validate"):
    with st.spinner("Analyzing..."):
        problem = run_problem_chain(idea)
        customer = run_customer_chain(idea)
        market = run_market_chain(idea)
        solution = run_solution_chain(idea)
        risk = run_risk_chain(idea)
        summary = run_summary_chain(
            idea, problem, customer, market, solution, risk
        )

    st.session_state["results"] = {...}
