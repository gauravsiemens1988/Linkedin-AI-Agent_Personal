import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_linkedin_post(title, source):
    prompt = f"""
Write a professional LinkedIn post (120–150 words) about the following green energy news.

Headline:
{title}

Guidelines:
- Start with a strong hook
- Explain why this matters for the energy transition
- Keep a professional, insightful tone
- End with a thoughtful question
- Add relevant hashtags
- Do NOT mention Google News or Gemini
"""

    response = model.generate_content(prompt)
    return response.text.strip()

