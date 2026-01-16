import replicate
import os
import requests

SDXL_MODEL = (
    "stability-ai/sdxl:"
    "39ed52f2a78e934b3ba6e2a89f5eec4c4d2a4f9dfb64e7b9a6c2d9f96c9c8a7b"
)

def generate_image(prompt, output_path="drafts/images/slide_1.png"):
    token = os.getenv("REPLICATE_API_TOKEN")
    if not token:
        raise RuntimeError("REPLICATE_API_TOKEN not set")

    client = replicate.Client(api_token=token)

    print("🎨 Generating image with Stable Diffusion (SDXL)...")

    output = client.run(
        SDXL_MODEL,
        input={
            "prompt": prompt,
            "width": 1024,
            "height": 576,
            "num_outputs": 1,
            "guidance_scale": 7.5,
            "num_inference_steps": 30,
        }
    )

    image_url = output[0]

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    response = requests.get(image_url, timeout=60)
    response.raise_for_status()

    with open(output_path, "wb") as f:
        f.write(response.content)

    print("🖼️ Image saved to", output_path)

