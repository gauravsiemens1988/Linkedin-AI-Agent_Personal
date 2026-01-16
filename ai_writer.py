import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_slide_structure(title):
    """
    Returns structured slide data in JSON format
    """

    prompt = f"""
From the news headline below, create a PRESENTATION structure.

NEWS HEADLINE:
{title}

OUTPUT JSON ONLY (no explanation, no markdown):

{{
  "slides": [
    {{
      "title": "Slide title (max 6 words)",
      "points": ["Point 1 (max 10 words)", "Point 2 (max 10 words)"]
    }}
  ]
}}

RULES:
- EXACTLY 6 slides
- Max 2 bullet points per slide
- Infographic / presentation tone
- Professional, simple language
- No emojis
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You create clean, professional presentation slides."},
            {"role": "user", "content": prompt}
        ]
    )

    return json.loads(response.choices[0].message.content.strip())



