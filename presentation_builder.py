from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
import os

def create_presentation(slides_data, image_folder="drafts/images"):
    prs = Presentation()
    blank_layout = prs.slide_layouts[6]

    for idx, slide_data in enumerate(slides_data, start=1):
        slide = prs.slides.add_slide(blank_layout)

        # -----------------------------
        # LEFT: IMAGE (if available)
        # -----------------------------
        image_path = os.path.join(image_folder, f"slide_{idx}.png")
        if os.path.exists(image_path):
            slide.shapes.add_picture(
                image_path,
                Inches(0.3),
                Inches(1.0),
                Inches(4.5),
                Inches(4.5)
            )

        # -----------------------------
        # RIGHT: TEXT AREA
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
        title_p = tf.paragraphs[0]
        title_p.text = slide_data["title"]
        title_p.font.size = Pt(30)
        title_p.font.bold = True
        title_p.font.color.rgb = RGBColor(32, 32, 32)

        # Bullet points
        for point in slide_data["points"]:
            p = tf.add_paragraph()
            p.text = point
            p.level = 1
            p.font.size = Pt(18)
            p.font.color.rgb = RGBColor(64, 64, 64)

    os.makedirs("drafts", exist_ok=True)
    output_path = "drafts/linkedin_carousel.pptx"
    prs.save(output_path)

    return output_path

