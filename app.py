import streamlit as st

from llm import call_llm
from validation_prompt import full_validation_prompt
from parser import parse_json

st.set_page_config(page_title="AI Idea Validator", layout="wide")

st.title("🚀 AI Idea Validator")
st.write("Validate your startup idea using VC-style thinking.")

idea = st.text_area(
    "Describe your startup idea",
    height=220,
    placeholder="Example: An AI tool that helps founders validate startup ideas before building them."
)

if st.button("Validate Idea") and idea.strip():

    with st.spinner("Analyzing your idea like a VC..."):
        prompt = full_validation_prompt(idea)
        response = call_llm(prompt)
        result = parse_json(response)

    if "error" in result:
        st.error("AI response could not be parsed.")
        st.text(result.get("raw_output", ""))
    else:
        tabs = st.tabs([
            "Problem",
            "Customer",
            "Market",
            "Solution",
            "Risks",
            "Summary"
        ])

        with tabs[0]:
            st.json(result["problem"])

        with tabs[1]:
            st.json(result["customer"])

        with tabs[2]:
            st.json(result["market"])

        with tabs[3]:
            st.json(result["solution"])

        with tabs[4]:
            st.json(result["risks"])

        with tabs[5]:
            st.json(result["summary"])
