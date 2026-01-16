from pptx import Presentation
from pptx.util import Inches, Pt
import os

def create_presentation(slides_data, image_path="drafts/images/slide_1.png"):
    prs = Presentation()

    for idx, slide_data in enumerate(slides_data):
        slide = prs.slides.add_slide(prs.slide_layouts[5])  # blank layout

        # -------------------------
        # Title
        # -------------------------
        title_box = slide.shapes.add_textbox(
            Inches(0.5), Inches(0.3), Inches(9), Inches(1)
        )
        title_tf = title_box.text_frame
        title_tf.text = slide_data["title"]
        title_tf.paragraphs[0].font.size = Pt(28)

        # -------------------------
        # Image only on first slide
        # -------------------------
        if idx == 0 and os.path.exists(image_path):
            slide.shapes.add_picture(
                image_path,
                Inches(0.5),
                Inches(1.3),
                width=Inches(9)
            )

        # -------------------------
        # Bullet points
        # -------------------------
        content_box = slide.shapes.add_textbox(
            Inches(0.8), Inches(4.5), Inches(8.5), Inches(2)
        )
        tf = content_box.text_frame
        tf.clear()

        for point in slide_data["points"]:
            p = tf.add_paragraph()
            p.text = point
            p.font.size = Pt(18)
            p.level = 0

    os.makedirs("drafts", exist_ok=True)
    output_path = "drafts/linkedin_carousel.pptx"
    prs.save(output_path)
    return output_path
