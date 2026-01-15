import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_linkedin_post(title, source):
    prompt = f"""
Write a professional LinkedIn post (120–150 words) about this green energy news.

Headline:
{title}

Guidelines:
- Start with a strong hook
- Explain why this matters for energy transition
- Use a professional, insightful tone
- End with a thoughtful question
- Add relevant hashtags

Do NOT mention Google News explicitly.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert LinkedIn content writer for energy and sustainability."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()
