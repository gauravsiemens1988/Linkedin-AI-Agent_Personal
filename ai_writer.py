import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_slide_structure(title, summary):
    """
    Generates presentation slides strictly from article content
    """

    # Fallback if summary is empty
    if not summary:
        summary = "No detailed article summary available."

    prompt = f"""
You are an analyst creating a FACT-BASED presentation.

ARTICLE TITLE:
{title}

ARTICLE CONTENT:
{summary}

TASK:
Create a presentation that reflects ONLY the information
present in the article content.

OUTPUT JSON ONLY (no explanation, no markdown):

{{
  "slides": [
    {{
      "title": "Fact-based slide title",
      "points": [
        "Concrete fact from article",
        "Another concrete fact"
      ]
    }}
  ]
}}

RULES:
- EXACTLY 6 slides
- Use ONLY information from ARTICLE CONTENT
- Prefer numbers, capacities, locations, approvals, actions
- Do NOT invent facts
- Do NOT repeat the article title on every slide
- Professional, neutral tone
- No emojis
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You extract factual insights from news articles."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return json.loads(response.choices[0].message.content.strip())




