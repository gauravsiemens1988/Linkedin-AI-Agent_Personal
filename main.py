import os
import json
from image_prompt_generator import generate_canva_style_prompt
from image_generator import generate_image
from presentation_builder import create_presentation

print("🚀 LinkedIn AI Agent started")

# -----------------------------
# LOAD ARTICLE
# -----------------------------
with open("latest_article.json", "r", encoding="utf-8") as f:
    article = json.load(f)

title = article["title"]
summary = article.get("summary", title)

print("📰 Article detected:", title)

# -----------------------------
# GENERATE IMAGE PROMPT
# -----------------------------
prompt = generate_canva_style_prompt(title, summary)

# -----------------------------
# GENERATE IMAGE (AUTO)
# -----------------------------
generate_image(prompt)

# -----------------------------
# PREPARE SLIDES
# -----------------------------
slides_data = [
    {
        "title": title,
        "points": [
            summary,
            "Strengthens India's clean energy ecosystem",
            "Supports solar, wind and grid infrastructure"
        ]
    }
]

# -----------------------------
# CREATE PRESENTATION
# -----------------------------
pptx_path = create_presentation(slides_data)

print("📊 Presentation generated:", pptx_path)
print("✅ LinkedIn AI Agent finished successfully")








