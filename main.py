import os
import json
from image_prompt_generator import generate_canva_style_prompt
from presentation_builder import create_presentation

print("🚀 LinkedIn AI Agent started")

# -----------------------------
# LOAD ARTICLE (SAFE)
# -----------------------------
article_file = "latest_article.json"

if not os.path.exists(article_file):
    print("❌ latest_article.json not found")
    exit(0)

with open(article_file, "r", encoding="utf-8") as f:
    article = json.load(f)

title = article.get("title", "Green Energy Update")
summary = article.get("summary", "India continues to expand its renewable energy capacity.")

print("📰 Article:", title)

# -----------------------------
# GENERATE CANVA IMAGE PROMPT
# -----------------------------
prompt = generate_canva_style_prompt(title, summary)

os.makedirs("drafts/images", exist_ok=True)

with open("drafts/images/image_prompt.txt", "w", encoding="utf-8") as f:
    f.write(prompt)

print("🎨 Canva image prompt saved")

# -----------------------------
# PREPARE SLIDE CONTENT
# -----------------------------
slides_data = [
    {
        "title": title,
        "points": [
            summary,
            "Strengthens India's renewable energy portfolio",
            "Supports solar, wind & grid infrastructure"
        ]
    }
]

# -----------------------------
# CREATE PRESENTATION
# -----------------------------
pptx_path = create_presentation(slides_data)

print(f"📊 Presentation generated: {pptx_path}")
print("✅ LinkedIn AI Agent finished successfully")









