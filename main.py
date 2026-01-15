import json
import os
from fetch_news import fetch_news
from ai_writer import generate_linkedin_post

print("🚀 LinkedIn AI Agent started")

# Fetch news
news = fetch_news()
print(f"📰 Fetched {len(news)} news items")

# Load memory
if os.path.exists("memory.json"):
    with open("memory.json", "r", encoding="utf-8") as f:
        memory = json.load(f)
else:
    memory = {}

# Detect new item
new_found = False

for item in news:
    if item["url"] not in memory:
        print("✅ New news detected:")
        print(item["title"])

        # Save to memory
        memory[item["url"]] = True

        # Generate AI LinkedIn draft
        post = generate_linkedin_post(item["title"], item["source"])

        # Save draft
        os.makedirs("drafts", exist_ok=True)
        with open("drafts/draft.txt", "w", encoding="utf-8") as f:
            f.write(post)

        print("📝 AI-written LinkedIn draft created in drafts/draft.txt")

        new_found = True
        break

# Save memory
with open("memory.json", "w", encoding="utf-8") as f:
    json.dump(memory, f, indent=2)

if not new_found:
    print("ℹ️ No new news found (agent still working)")











