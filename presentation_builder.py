from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
import os

def create_presentation(slides_data, image_path=None):
    prs = Presentation()
    blank_layout = prs.slide_layouts[6]

    for slide in slides_data:
        slide_obj = prs.slides.add_slide(blank_layout)

        # Optional background image
        if image_path and os.path.exists(image_path):
            slide_obj.shapes.add_picture(
                image_path,
                Inches(0),
                Inches(0),
                width=prs.slide_width,
                height=prs.slide_height
            )

        # Title box
        title_box = slide_obj.shapes.add_textbox(
            Inches(0.5), Inches(0.5), Inches(9), Inches(1.2)
        )
        title_tf = title_box.text_frame
        title_tf.clear()
        p = title_tf.paragraphs[0]
        p.text = slide["title"]
        p.font.size = Pt(34)
        p.font.bold = True
        p.font.color.rgb = RGBColor(0, 0, 0)

        # Bullet points
        content_box = slide_obj.shapes.add_textbox(
            Inches(0.8), Inches(2), Inches(8.5), Inches(4)
        )
        content_tf = content_box.text_frame
        content_tf.clear()

        for point in slide["points"]:
            para = content_tf.add_paragraph()
            para.text = point
            para.level = 1
            para.font.size = Pt(20)

    os.makedirs("drafts", exist_ok=True)
    file_path = "drafts/linkedin_carousel.pptx"
    prs.save(file_path)

    return file_path
