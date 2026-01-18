def problem_prompt():
    return """
You are a startup analyst.

Evaluate the PROBLEM behind this idea:

{idea}

Return JSON only:
{
  "problem_summary": "",
  "pain_intensity": "",
  "problem_clarity_score": 1-10,
  "current_workarounds": [],
  "key_assumption": "",
  "validation_question": ""
}
"""
