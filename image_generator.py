import replicate
import os
import requests

MODEL = "stability-ai/sdxl-turbo"

def generate_image(prompt, output_path="drafts/images/slide_1.png"):
    token = os.getenv("REPLICATE_API_TOKEN")
    if not token:
        raise RuntimeError("REPLICATE_API_TOKEN not set")

    client = replicate.Client(api_token=token)

    print("🎨 Generating image with Stable Diffusion (SDXL Turbo)...")

    output = client.run(
        MODEL,
        input={
            "prompt": prompt,
            "num_inference_steps": 4,   # turbo requires low steps
            "guidance_scale": 2.0       # turbo optimized
        }
    )

    # SDXL Turbo returns a list of image URLs
    image_url = output[0]

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    response = requests.get(image_url, timeout=60)
    response.raise_for_status()

    with open(output_path, "wb") as f:
        f.write(response.content)

    print("🖼️ Image saved to", output_path)
