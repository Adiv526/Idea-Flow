def customer_prompt():
    return """
Identify the strongest early adopter for this startup idea:

{idea}

Return JSON only:

{
  "ideal_customer": "",
  "customer_context": "",
  "why_they_care": "",
  "early_adopter_strength": 1-10,
  "wrong_customer_risk": ""
}
"""
