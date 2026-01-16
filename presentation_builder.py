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

    base_dir = os.getcwd()
    image_folder_path = os.path.join(base_dir, image_folder)

    # -----------------------------
    # FIND IMAGE (MANDATORY CHECK)
    # -----------------------------
    image_path = None
    if os.path.exists(image_folder_path):
        for file in sorted(os.listdir(image_folder_path)):
            if file.lower().endswith(".png"):
                image_path = os.path.join(image_folder_path, file)
                break

    print(f"DEBUG: image_path = {image_path}")

    # -----------------------------
    # CREATE SLIDES
    # -----------------------------
    for idx, slide_data in enumerate(slides_data, start=1):
        slide = prs.slides.add_slide(blank_layout)

        # -----------------------------
        # IMAGE AS FULL BACKGROUND
        # -----------------------------
        if image_path and os.path.exists(image_path):
            slide.shapes.add_picture(
                image_path,
                Inches(0),
                Inches(0),
                width=prs.slide_width,
                height=prs.slide_height
            )
        else:
            print(f"⚠️ No image applied on slide {idx}")

        # -----------------------------
        # TEXT OVERLAY BOX
        # -----------------------------
        textbox = slide.shapes.add_textbox(
            Inches(0.8),
            Inches(0.8),
            prs.slide_width - Inches(1.6),
            Inches(2.5)
        )
        tf = textbox.text_frame
        tf.clear()

        # Title
        title_p = tf.paragraphs[0]
        title_p.text = slide_data["title"]
        title_p.font.size = Pt(28)
        title_p.font.bold = True
        title_p.font.color.rgb = RGBColor(255, 255, 255)

        # Bullets
        for point in slide_data["points"]:
            p = tf.add_paragraph()
            p.text = point
            p.font.size = Pt(18)
            p.font.color.rgb = RGBColor(240, 240, 240)
            p.level = 1

        # -----------------------------
        # LOGO WATERMARK
        # -----------------------------
        logo_full_path = os.path.join(base_dir, logo_path)
        if os.path.exists(logo_full_path):
            slide.shapes.add_picture(
                logo_full_path,
                prs.slide_width - Inches(1.8),
                prs.slide_height - Inches(0.9),
                width=Inches(1.5)
            )

    # -----------------------------
    # SAVE PPT
    # -----------------------------
    os.makedirs("drafts", exist_ok=True)
    output_path = os.path.join("drafts", "linkedin_carousel.pptx")
    prs.save(output_path)

    return output_path



