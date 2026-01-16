import os

def generate_image(prompt, output_path="drafts/images/slide_1.png"):
    """
    Semi-automation mode:
    - Writes image prompt
    - User manually generates image in Canva / ChatGPT
    - CI never fails
    """

    os.makedirs("drafts/images", exist_ok=True)

    prompt_path = "drafts/images/image_prompt.txt"
    with open(prompt_path, "w", encoding="utf-8") as f:
        f.write(prompt)

    print("📝 Image prompt generated")
    print("👉 Open drafts/images/image_prompt.txt")
    print("👉 Generate image in Canva / ChatGPT")
    print("👉 Save image as drafts/images/slide_1.png")

