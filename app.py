import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


import streamlit as st

from chains.problem_chain import run_problem_chain
from customer_chain import run_customer_chain
from market_chain import run_market_chain
from chains.solution_chain import run_solution_chain
from chains.risk_chain import run_risk_chain
from chains.summary_chain import run_summary_chain

st.set_page_config(page_title="AI Idea Validator", layout="wide")

st.title("🚀 AI Idea Validator")
st.write("Validate your startup idea using VC-style thinking.")

idea = st.text_area(
    "Describe your startup idea",
    height=200,
    placeholder="Example: An AI tool that helps solo founders validate startup ideas before building..."
)

if st.button("Validate Idea") and idea.strip():

    with st.spinner("Analyzing your idea like a VC..."):
        problem = run_problem_chain(idea)
        customer = run_customer_chain(idea)
        market = run_market_chain(idea)
        solution = run_solution_chain(idea)
        risk = run_risk_chain(idea)
        summary = run_summary_chain(
            idea, problem, customer, market, solution, risk
        )

    tabs = st.tabs([
        "Problem", "Customer", "Market",
        "Solution", "Risks", "Summary"
    ])

    with tabs[0]:
        st.json(problem)

    with tabs[1]:
        st.json(customer)

    with tabs[2]:
        st.json(market)

    with tabs[3]:
        st.json(solution)

    with tabs[4]:
        st.json(risk)

    with tabs[5]:
        st.json(summary)
