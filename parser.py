import json
import re

def parse_json(text: str):
    try:
        match = re.search(r"\{.*\}", text, re.S)
        if not match:
            return {"error": "No JSON found", "raw": text}

        return json.loads(match.group())
    except Exception as e:
        return {"error": "JSON parse failed", "raw": text}
