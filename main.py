import json
import os

from fetch_news import fetch_news
from ai_writer import generate_slide_structure
from presentation_builder import create_presentation

print("🚀 LinkedIn AI Agent started")

MEMORY_FILE = "memory.json"
IMAGE_FOLDER = "drafts/images"

# -----------------------------
# LOAD MEMORY (SAFE)
# -----------------------------
memory = {}
if os.path.exists(MEMORY_FILE):
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if content:
                memory = json.loads(content)
    except Exception:
        print("⚠️ memory.json invalid, resetting.")
        memory = {}

# -----------------------------
# FETCH NEWS
# -----------------------------
news_items = fetch_news()
print(f"📰 Fetched {len(news_items)} news items")

new_item_found = False

# -----------------------------
# PROCESS FIRST NEW ARTICLE
# -----------------------------
for item in news_items:
    url = item.get("url")
    title = item.get("title")
    summary = item.get("summary", "")

    if not url or not title:
        continue

    if url in memory:
        continue

    print("✅ New article detected:")
    print(title)

    # Mark article as processed
    memory[url] = True

    # -----------------------------
    # GENERATE SLIDE STRUCTURE
    # -----------------------------
    slide_json = generate_slide_structure(
        title=title,
        summary=summary
    )

    slides_data = slide_json.get("slides", [])

    if not slides_data:
        print("⚠️ No slide data generated")
        break

    # -----------------------------
    # CREATE PRESENTATION
    # (USES EXISTING IMAGES)
    # -----------------------------
    pptx_path = create_presentation(
        slides_data=slides_data,
        image_folder=IMAGE_FOLDER
    )

    print(f"📊 Presentation generated: {pptx_path}")

    new_item_found = True
    break

# -----------------------------
# SAVE MEMORY
# -----------------------------
with open(MEMORY_FILE, "w", encoding="utf-8") as f:
    json.dump(memory, f, indent=2)

if not new_item_found:
    print("ℹ️ No new news found")

print("✅ LinkedIn AI Agent finished successfully")











