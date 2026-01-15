import json
import os
from fetch_news import fetch_news

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

        memory[item["url"]] = True
        new_found = True
        break

# Save memory
with open("memory.json", "w", encoding="utf-8") as f:
    json.dump(memory, f, indent=2)

if not new_found:
    print("ℹ️ No new news found (agent still working)")






