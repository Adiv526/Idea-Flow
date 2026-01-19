def full_validation_prompt(idea):
    return f"""
You are a venture capital analyst.

Evaluate the startup idea below using professional VC frameworks.

Startup idea:
{idea}

Analyze and return a SINGLE JSON object with the following structure:

{{
  "problem": {{
    "summary": "",
    "pain_intensity": "low | medium | high",
    "clarity_score": 1-10,
    "current_workarounds": [],
    "key_assumption": ""
  }},
  "customer": {{
    "ideal_customer": "",
    "why_they_care": "",
    "early_adopter_strength": 1-10
  }},
  "market": {{
    "market_type": "niche | medium | large | unclear",
    "market_reasoning": "",
    "market_score": 1-10
  }},
  "solution": {{
    "differentiation_strength": 1-10,
    "is_10x_candidate": "yes | maybe | no",
    "solution_risk": ""
  }},
  "risks": {{
    "top_risks": [],
    "hardest_part": ""
  }},
  "summary": {{
    "overall_strength": "weak | moderate | strong",
    "biggest_unknown": "",
    "next_30_day_plan": []
  }}
}}

Return ONLY valid JSON.
"""
