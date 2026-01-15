import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_image(prompt, filename):
    os.makedirs("drafts/images", exist_ok=True)

    result = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="1024x1024"
    )

    image_base64 = result.data[0].b64_json
    image_bytes = base64.b64decode(image_base64)

    file_path = f"drafts/images/{filename}"

    with open(file_path, "wb") as f:
        f.write(image_bytes)

    return file_path
