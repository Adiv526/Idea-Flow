def market_prompt():
    return """
Evaluate the market sanity for this startup idea:

{idea}

Return JSON only:

{
  "market_type": "niche | medium | large | unclear",
  "market_reasoning": "",
  "trend_support": "",
  "market_score": 1-10,
  "market_assumption": ""
}
"""
