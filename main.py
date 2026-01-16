import os
import json
import feedparser
from image_prompt_generator import generate_canva_style_prompt
from image_generator import generate_image
from presentation_builder import create_presentation

print("🚀 LinkedIn AI Agent started")

# ---------------------------------------
# Fetch latest green-energy news
# ---------------------------------------
RSS_URL = (
    "https://news.google.com/rss/search?"
    "q=green+energy+OR+solar+OR+wind+OR+hydrogen+OR+renewable"
    "&hl=en-IN&gl=IN&ceid=IN:en"
)

print("📰 Fetching latest green energy news...")
feed = feedparser.parse(RSS_URL)

news_items = []
for entry in feed.entries[:5]:
    news_items.append({
        "title": entry.title,
        "summary": entry.get("summary", entry.title),
        "url": entry.link
    })

if not news_items:
    print("⚠️ No news found")
    exit(0)

article = news_items[0]
title = article["title"]
summary = article["summary"]

print("🟢 Selected article:")
print(title)

# ---------------------------------------
# Generate Canva-style image prompt
# ---------------------------------------
prompt = generate_canva_style_prompt(title, summary)
generate_image(prompt)

# ---------------------------------------
# Slide content
# ---------------------------------------
slides_data = [
    {
        "title": title,
        "points": [
            summary,
            "Strategic boost to India’s renewable ecosystem",
            "Supports long-term clean energy transition"
        ]
    }
]

# ---------------------------------------
# Build presentation
# ---------------------------------------
pptx_path = create_presentation(slides_data)

print(f"📊 Presentation generated: {pptx_path}")
print("✅ LinkedIn AI Agent finished successfully")



