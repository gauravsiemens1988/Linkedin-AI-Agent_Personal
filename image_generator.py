import replicate
import os
import requests

MODEL = "bytedance/sdxl-lightning-4step"

def generate_image(prompt, output_path="drafts/images/slide_1.png"):
    token = os.getenv("REPLICATE_API_TOKEN")
    if not token:
        raise RuntimeError("REPLICATE_API_TOKEN not set")

    client = replicate.Client(api_token=token)

    print("🎨 Generating image with SDXL Lightning (Replicate)...")

    output = client.run(
        MODEL,
        input={
            "prompt": prompt,
            "negative_prompt": "text, watermark, logo, blurry",
            "num_inference_steps": 4,
            "guidance_scale": 1.5,
            "width": 1024,
            "height": 576
        }
    )

    # Replicate returns list of image URLs
    image_url = output[0]

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    response = requests.get(image_url, timeout=60)
    response.raise_for_status()

    with open(output_path, "wb") as f:
        f.write(response.content)

    print("🖼️ Image saved to", output_path)

