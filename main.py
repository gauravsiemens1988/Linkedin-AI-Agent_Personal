import os
import json
import feedparser
from image_prompt_generator import generate_canva_style_prompt
from image_generator import generate_image
from presentation_builder import create_presentation

print("🚀 LinkedIn AI Agent started")

# --------------------------------------------------
# STEP 1: FETCH LATEST GREEN ENERGY NEWS
# --------------------------------------------------
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
        "url": entry.link,
        "source": "Google News"
    })

if not news_items:
    print("⚠️ No news fetched, stopping agent")
    exit(0)

# Save for traceability
with open("latest_news.json", "w", encoding="utf-8") as f:
    json.dump(news_items, f, indent=2, ensure_ascii=False)

print(f"✅ Fetched {len(news_items)} news items")

# --------------------------------------------------
# STEP 2: PICK LATEST ARTICLE
# --------------------------------------------------
article = news_items[0]
title = article["title"]
summary = article["summary"]

print("🟢 Selected article:")
print(title)

# --------------------------------------------------
# STEP 3: GENERATE CANVA-STYLE IMAGE PROMPT
# --------------------------------------------------
prompt = generate_canva_style_prompt(title, summary)

# --------------------------------------------------
# STEP 4: AUTO-GENERATE IMAGE (STABLE DIFFUSION)
# --------------------------------------------------
generate_image(prompt)

# --------------------------------------------------
# STEP 5: PREPARE SLIDE CONTENT
# --------------------------------------------------
slides_data = [
    {
        "title": title,
        "points": [
            summary,
            "Strengthens India’s renewable energy ecosystem",
            "Supports long-term clean power infrastructure"
        ]
    }
]

# --------------------------------------------------
# STEP 6: CREATE PRESENTATION
# --------------------------------------------------
pptx_path = create_presentation(slides_data)

print(f"📊 Presentation generated: {pptx_path}")
print("✅ LinkedIn AI Agent finished successfully")





