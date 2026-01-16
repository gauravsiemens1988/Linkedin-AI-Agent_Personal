import replicate
import os
import requests

def generate_image(prompt, output_path="drafts/images/slide_1.png"):
    token = os.getenv("REPLICATE_API_TOKEN")
    if not token:
        raise RuntimeError("REPLICATE_API_TOKEN not set")

    client = replicate.Client(api_token=token)

    print("🎨 Generating image with Stable Diffusion...")

    output = client.run(
        "stability-ai/sdxl",
        input={
            "prompt": prompt,
            "width": 1024,
            "height": 576,
            "num_outputs": 1,
            "guidance_scale": 7.5,
            "num_inference_steps": 30
        }
    )

    image_url = output[0]

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    img = requests.get(image_url).content
    with open(output_path, "wb") as f:
        f.write(img)

    print("🖼️ Image saved to", output_path)

