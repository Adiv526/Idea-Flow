def summary_prompt():
    return """
You are a VC analyst.

Based on the analysis below, produce a concise validation summary.

Idea:
{idea}

Problem:
{problem}

Customer:
{customer}

Market:
{market}

Solution:
{solution}

Risks:
{risk}

Return JSON only:

{
  "overall_strength": "weak | moderate | strong",
  "why_this_could_work": [],
  "why_this_might_fail": [],
  "biggest_unknown": "",
  "next_30_day_validation_plan": []
}
"""
