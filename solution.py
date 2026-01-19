def solution_prompt():
    return f"""
Evaluate the proposed solution approach:

{idea}

Return JSON only:

{{
  "solution_summary": "",
  "differentiation_strength": 1-10,
  "is_10x_better_candidate": "yes | maybe | no",
  "time_to_value": "immediate | short | long",
  "solution_risk": ""
}}
"""
