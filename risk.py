def risk_prompt():
    return """
Identify the biggest risks for this startup idea:

{idea}

Return JSON only:

{{
  "top_risks": [],
  "hardest_part_to_execute": "",
  "feasibility_score": 1-10,
  "why_most_founders_fail_here": ""
}}
"""
