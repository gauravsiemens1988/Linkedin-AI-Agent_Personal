import json
import os
from fetch_news import fetch_news
from ai_writer import generate_linkedin_post

print("🚀 LinkedIn AI Agent started")

# Step 1: Fetch latest news
news_items = fetch_news()
print(f"📰 Fetched {len(news_items)} news items")

# Step 2: Load memory (to avoid duplicates)
MEMORY_FILE = "memory.json"

if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        memory = json.load(f)
else:
    memory = {}

new_item_found = False

# Step 3: Detect new news item
for item in news_items:
    url = item.get("url")

    if not url:
        continue

    if url not in memory:
        print("✅ New news detected:")
        print(item["title"])

        # Mark as processed
        memory[url] = True

        # Step 4: Generate infographic carousel content
        carousel_content = generate_linkedin_post(
            title=item["title"],
            source=item.get("source", "")
        )

        # Step 5: Save outputs
        os.makedirs("drafts", exist_ok=True)

        with open("drafts/carousel_slides.txt", "w", encoding="utf-8") as f:
            f.write(carousel_content)

        print("🖼️ Infographic carousel content generated")
        new_item_found = True
        break

# Step 6: Save updated memory
with open(MEMORY_FILE, "w", encoding="utf-8") as f:
    json.dump(memory, f, indent=2)

if not new_item_found:
    print("ℹ️ No new news found in this run")

print("✅ LinkedIn AI Agent finished successfully")










