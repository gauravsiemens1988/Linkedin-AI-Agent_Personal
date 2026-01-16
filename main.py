import json
import os

from fetch_news import fetch_news
from ai_writer import generate_slide_structure
from presentation_builder import create_presentation

print("🚀 LinkedIn AI Agent started")

MEMORY_FILE = "memory.json"

# Load memory
if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        memory = json.load(f)
else:
    memory = {}

# Fetch news
news_items = fetch_news()
print(f"📰 Fetched {len(news_items)} news items")

new_item_found = False

for item in news_items:
    url = item.get("url")
    title = item.get("title")

    if not url or not title:
        continue

    if url in memory:
        continue

    print("✅ New article detected:")
    print(title)

    # Mark as processed
    memory[url] = True

    # Generate slide structure
    slide_json = generate_slide_structure(title)
    slides_data = slide_json["slides"]

    # Optional image (use first generated image if exists)
    image_path = None
    if os.path.exists("drafts/images/slide_1.png"):
        image_path = "drafts/images/slide_1.png"

    pptx_path = create_presentation(
        slides_data=slides_data,
        image_path=image_path
    )

    print(f"📊 Presentation generated: {pptx_path}")

    new_item_found = True
    break

# Save memory
with open(MEMORY_FILE, "w", encoding="utf-8") as f:
    json.dump(memory, f, indent=2)

if not new_item_found:
    print("ℹ️ No new news found")

print("✅ LinkedIn AI Agent finished successfully")









