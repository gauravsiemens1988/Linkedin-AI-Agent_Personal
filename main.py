import json
import os

MEMORY_FILE = "memory.json"

# Load memory
if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r") as f:
        memory = json.load(f)
else:
    memory = {}

# Find first NEW article
selected_article = None
for entry in feed.entries:
    if entry.link not in memory:
        selected_article = entry
        break

if not selected_article:
    print("ℹ️ No new article found today. Exiting.")
    exit(0)

# Mark article as processed
memory[selected_article.link] = True
with open(MEMORY_FILE, "w") as f:
    json.dump(memory, f, indent=2)

# Use selected article
article = selected_article


