import json
import re

def parse_json(text: str):
    try:
        match = re.search(r"\{.*\}", text, re.S)
        if not match:
            return {"error": "No JSON found"}

        json_str = match.group()
        return json.loads(json_str)
    except Exception as e:
        return {
            "error": "JSON parsing failed",
            "raw_output": text
        }
