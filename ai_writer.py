import os
import json
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_slide_structure(title, summary):
    """
    Generate a 6-slide LinkedIn carousel based strictly on article content.
    All slides share the SAME headline (article title).
    """

    if not summary or summary.strip() == "":
        summary = "Article summary not available. Use the title context carefully."

    prompt = f"""
You are an analyst creating a FACT-BASED LinkedIn presentation.

ARTICLE TITLE:
{title}

ARTICLE CONTENT:
{summary}

TASK:
Create a LinkedIn carousel presentation.

OUTPUT FORMAT:
Return ONLY valid JSON. No explanations. No markdown.

STRUCTURE:
- EXACTLY 6 slides
- ALL slides must use the SAME title: "{title}"
- Each slide must highlight a DIFFERENT factual point from the article

RULES:
- Use ONLY information from ARTICLE CONTENT
- Prefer concrete facts: numbers, capacity, locations, approvals, partnerships
- Do NOT invent or assume facts
- Do NOT add opinions or marketing language
- Professional, neutral tone
- No emojis

JSON FORMAT:
{{
  "slides": [
    {{
      "title": "{title}",
      "points": [
        "Factual point derived from the article",
        "Another factual point derived from the article"
      ]
    }}
  ]
}}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You extract factual insights from news articles and structure them into presentations."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    content = response.choices[0].message.content.strip()

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        # Fail-safe fallback (never crash pipeline)
        return {
            "slides": [
                {
                    "title": title,
                    "points": [
                        "Key details could not be parsed correctly.",
                        "Please review the article summary."
                    ]
                }
            ] * 6
        }




