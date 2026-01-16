import os
import json
from image_prompt_generator import generate_canva_style_prompt
from image_generator import generate_image
from presentation_builder import create_presentation

print("🚀 LinkedIn AI Agent started")

# --------------------------------------------------
# LOAD LATEST NEWS (EXISTING FILE)
# --------------------------------------------------
NEWS_FILE = "latest_news.json"

if not os.path.exists(NEWS_FILE):
    print("❌ latest_news.json not found")
    exit(0)

with open(NEWS_FILE, "r", encoding="utf-8") as f:
    news_items = json.load(f)

if not news_items:
    print("⚠️ No news items found")
    exit(0)

# Pick the FIRST article (latest)
article = news_items[0]

title = article.get("title", "Green Energy Update")
summary = article.get(
    "summary",
    "India continues to strengthen its renewable energy ecosystem."
)

print("📰 Article selected:")
print(title)

# --------------------------------------------------
# GENERATE CANVA-STYLE IMAGE PROMPT
# --------------------------------------------------
prompt = generate_canva_style_prompt(title, summary)

# --------------------------------------------------
# AUTO-GENERATE IMAGE (STABLE DIFFUSION)
# --------------------------------------------------
generate_image(prompt)

# --------------------------------------------------
# PREPARE SLIDE CONTENT
# --------------------------------------------------
slides_data = [
    {
        "title": title,
        "points": [
            summary,
            "Strengthens India’s clean energy portfolio",
            "Supports long-term renewable infrastructure",
        ]
    }
]

# --------------------------------------------------
# CREATE PRESENTATION
# --------------------------------------------------
pptx_path = create_presentation(slides_data)

print(f"📊 Presentation generated: {pptx_path}")
print("✅ LinkedIn AI Agent finished successfully")







