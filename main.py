import json
import os
import base64

from fetch_news import fetch_news
from ai_writer import generate_linkedin_post
from openai import OpenAI

print("🚀 LinkedIn AI Agent started")

# -----------------------------
# CONFIG
# -----------------------------
MEMORY_FILE = "memory.json"
DRAFT_DIR = "drafts"
IMAGE_DIR = os.path.join(DRAFT_DIR, "images")

os.makedirs(DRAFT_DIR, exist_ok=True)
os.makedirs(IMAGE_DIR, exist_ok=True)

# OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# -----------------------------
# STEP 1: FETCH NEWS
# -----------------------------
news_items = fetch_news()
print(f"📰 Fetched {len(news_items)} news items")

# -----------------------------
# STEP 2: LOAD MEMORY
# -----------------------------
if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        memory = json.load(f)
else:
    memory = {}

new_item_found = False

# -----------------------------
# STEP 3: PROCESS NEW ARTICLE
# -----------------------------
for item in news_items:
    url = item.get("url")
    title = item.get("title")

    if not url or not title:
        continue

    if url in memory:
        continue

    print("✅ New news detected:")
    print(title)

    # Mark as processed
    memory[url] = True

    # -----------------------------
    # STEP 4: GENERATE INFOGRAPHIC CONTENT
    # -----------------------------
    carousel_text = generate_linkedin_post(
        title=title,
        source=item.get("source", "")
    )

    with open(os.path.join(DRAFT_DIR, "carousel_slides.txt"), "w", encoding="utf-8") as f:
        f.write(carousel_text)

    print("🖼️ Infographic slide text & prompts generated")

    # -----------------------------
    # STEP 5: EXTRACT IMAGE PROMPTS
    # -----------------------------
    image_prompts = []
    current_prompt = []

    for line in carousel_text.splitlines():
        if line.strip().startswith("Image Prompt:"):
            current_prompt = [line.replace("Image Prompt:", "").strip()]
        elif current_prompt and line.strip():
            current_prompt.append(line.strip())
        elif current_prompt and not line.strip():
            image_prompts.append(" ".join(current_prompt))
            current_prompt = []

    if current_prompt:
        image_prompts.append(" ".join(current_prompt))

    # -----------------------------
    # STEP 6: GENERATE IMAGES USING CHATGPT
    # -----------------------------
    for idx, prompt in enumerate(image_prompts, start=1):
        print(f"🎨 Generating image for Slide {idx}")

        result = client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size="1024x1024"
        )

        image_base64 = result.data[0].b64_json
        image_bytes = base64.b64decode(image_base64)

        image_path = os.path.join(IMAGE_DIR, f"slide_{idx}.png")

        with open(image_path, "wb") as img_file:
            img_file.write(image_bytes)

    print(f"🖼️ {len(image_prompts)} images generated successfully")

    new_item_found = True
    break

# -----------------------------
# STEP 7: SAVE MEMORY
# -----------------------------
with open(MEMORY_FILE, "w", encoding="utf-8") as f:
    json.dump(memory, f, indent=2)

if not new_item_found:
    print("ℹ️ No new news found in this run")

print("✅ LinkedIn AI Agent completed successfully")











