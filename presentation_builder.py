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

    # -----------------------------
    # RESOLVE IMAGE PATH (SAFE)
    # -----------------------------
    base_dir = os.getcwd()
    image_folder_path = os.path.join(base_dir, image_folder)

    image_path = None
    if os.path.exists(image_folder_path):
        for file in sorted(os.listdir(image_folder_path)):
            if file.lower().endswith(".png"):
                image_path = os.path.join(image_folder_path, file)
                break

    if image_path:
        print(f"🖼️ Using image: {image_path}")
    else:
        print("⚠️ No image found for slides")

    # -----------------------------
    # CREATE SLIDES
    # -----------------------------
    for slide_data in slides_data:
        slide = prs.slides.add_slide(blank_layout)

        # -----------------------------
        # IMAGE (LEFT SIDE)
        # -----------------------------
        if image_path and os.path.exists(image_path):
            slide.shapes.add_picture(
                image_path,
                Inches(0.3),
                Inches(1.0),
                width=Inches(4.5)
            )

        # -----------------------------
        # TEXT (RIGHT SIDE)
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
        title_para = tf.paragraphs[0]
        title_para.text = slide_data["title"]
        title_para.font.size = Pt(28)
        title_para.font.bold = True
        title_para.font.color.rgb = RGBColor(32, 32, 32)

        # Bullet points
        for point in slide_data["points"]:
            p = tf.add_paragraph()
            p.text = point
            p.level = 1
            p.font.size = Pt(18)

        # -----------------------------
        # LOGO WATERMARK
        # -----------------------------
        logo_full_path = os.path.join(base_dir, logo_path)
        if logo_path and os.path.exists(logo_full_path):
            slide.shapes.add_picture(
                logo_full_path,
                prs.slide_width - Inches(1.8),
                prs.slide_height - Inches(0.9),
                width=Inches(1.5)
            )

    # -----------------------------
    # SAVE PPT
    # -----------------------------
    output_dir = os.path.join(base_dir, "drafts")
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, "linkedin_carousel.pptx")
    prs.save(output_path)

    return output_path


