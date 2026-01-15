import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_linkedin_post(title, source):
    prompt = f"""
Write a professional LinkedIn post (120–150 words) about the following green energy news.

Headline:
{title}

Guidelines:
- Start with a strong hook
- Explain why this matters for the energy transition
- Use a professional, insightful tone
- End with a thoughtful question
- Add relevant hashtags
- Do NOT mention Google News or Gemini
"""

    response = client.models.generate_content(
        model="gemini-1.0-pro",
        contents=prompt
    )

    return response.text.strip()


