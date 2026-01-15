import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_linkedin_post(title, source):
    """
    Generates infographic-style LinkedIn carousel content
    along with ChatGPT-ready image prompts.
    """

    prompt = f"""
You are a LinkedIn content strategist and infographic designer
specializing in energy, sustainability, and infrastructure.

TASK:
Create an INFOGRAPHIC-STYLE LinkedIn carousel based on the news headline below.

NEWS HEADLINE:
{title}

CREATE EXACTLY 6 SLIDES.

For EACH slide provide:
- Slide Heading (max 6 words)
- Slide Text (max 12 words)
- Visual Concept (icons / charts / illustration idea)
- Image Prompt (for ChatGPT image generation)

STYLE RULES:
- Text must be short, visual, and infographic-friendly
- No paragraphs
- No emojis
- No marketing language
- Audience: CXOs, engineers, policymakers
- Do NOT mention Google News or OpenAI

FORMAT STRICTLY LIKE THIS:

SLIDE 1
Heading:
Text:
Visual:
Image Prompt:

SLIDE 2
Heading:
Text:
Visual:
Image Prompt:

SLIDE 3
Heading:
Text:
Visual:
Image Prompt:

SLIDE 4
Heading:
Text:
Visual:
Image Prompt:

SLIDE 5
Heading:
Text:
Visual:
Image Prompt:

SLIDE 6
Heading:
Text:
Visual:
Image Prompt:
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You design clean, professional infographic carousels for LinkedIn."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content.strip()



