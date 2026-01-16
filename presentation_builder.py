from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
import os

def create_presentation(
    slides_data,
    image_folder="drafts/images",
    logo_path="assets/logo_watermark.png"
):
    prs = Presentation()
    layout = prs.slide_layouts[1]  # Title + Content (SAFE)

    base_dir = os.getcwd()
    image_folder_path = os.path.join(base_dir, image_folder)

    # -----------------------------
    # FIND FIRST IMAGE (MANDATORY)
    # -----------------------------
    image_path = None
    if os.path.exists(image_folder_path):
        for f in sorted(os.listdir(image_folder_path)):
            if f.lower().endswith(".png"):
                image_path = os.path.join(image_folder_path, f)
                break

    print(f"DEBUG: Image path resolved -> {image_path}")

    for slide_data in slides_data:
        slide = prs.slides.add_slide(layout)

        # -----------------------------
        # TITLE
        # -----------------------------
        title = slide.shapes.title
        title.text = slide_data["title"]
        title.text_frame.paragraphs[0].font.size = Pt(28)
        title.text_frame.paragraphs[0].font.bold = True

        # -----------------------------
        # CONTENT PLACEHOLDER
        # -----------------------------
        content = slide.placeholders[1]
        tf = content.text_frame
        tf.clear()

        # -----------------------------
        # INSERT IMAGE *INSIDE PLACEHOLDER*
        # -----------------------------
        if image_path and os.path.exists(image_path):
            content.insert_picture(image_path)
        else:
            tf.text = "⚠️ Image missing"

        # -----------------------------
        # ADD BULLETS BELOW IMAGE
        # -----------------------------
        for point in slide_data["points"][:4]:
            p = tf.add_paragraph()
            p.text = point
            p.level = 1
            p.font.size = Pt(16)

        # -----------------------------
        # LOGO WATERMARK
        # -----------------------------
        logo_full = os.path.join(base_dir, logo_path)
        if os.path.exists(logo_full):
            slide.shapes.add_picture(
                logo_full,
                prs.slide_width - Inches(1.8),
                prs.slide_height - Inches(0.9),
                width=Inches(1.4)
            )

    os.makedirs("drafts", exist_ok=True)
    output = "drafts/linkedin_carousel.pptx"
    prs.save(output)

    return output



