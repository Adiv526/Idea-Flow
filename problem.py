def problem_prompt(idea):
    return f"""
Evaluate the PROBLEM behind this startup idea:

{idea}

Return JSON only:

{{
  "problem_summary": "",
  "pain_intensity": "low | medium | high",
  "problem_clarity_score": 1-10,
  "current_workarounds": [],
  "key_assumption": "",
  "validation_question": ""
}}
"""
