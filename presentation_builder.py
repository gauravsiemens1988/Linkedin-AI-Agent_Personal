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
    blank_layout = prs.slide_layouts[6]

    # Pick FIRST available image (fallback-safe)
    image_path = None
    if os.path.exists(image_folder):
        for file in sorted(os.listdir(image_folder)):
            if file.endswith(".png"):
                image_path = os.path.join(image_folder, file)
                break

    for slide_data in slides_data:
        slide = prs.slides.add_slide(blank_layout)

        # -----------------------------
        # IMAGE (LEFT) – SAME IMAGE SAFE MODE
        # -----------------------------
        if image_path and os.path.exists(image_path):
            slide.shapes.add_picture(
                image_path,
                Inches(0.3),
                Inches(1.0),
                Inches(4.5),
                Inches(4.5)
            )

        # -----------------------------
        # TEXT (RIGHT)
        # -----------------------------
        text_box = slide.shapes.add_textbox(
            Inches(5.0),
            Inches(1.0),
            Inches(4.5),
            Inches(4.5)
        )
        tf = text_box.text_frame
        tf.clear()

        # Title
        p = tf.paragraphs[0]
        p.text = slide_data["title"]
        p.font.size = Pt(30)
        p.font.bold = True
        p.font.color.rgb = RGBColor(32, 32, 32)

        # Bullets
        for point in slide_data["points"]:
            bp = tf.add_paragraph()
            bp.text = point
            bp.level = 1
            bp.font.size = Pt(18)

        # -----------------------------
        # LOGO WATERMARK
        # -----------------------------
        if logo_path and os.path.exists(logo_path):
            slide.shapes.add_picture(
                logo_path,
                prs.slide_width - Inches(1.8),
                prs.slide_height - Inches(0.9),
                width=Inches(1.5)
            )

    os.makedirs("drafts", exist_ok=True)
    output = "drafts/linkedin_carousel.pptx"
    prs.save(output)

    return output


