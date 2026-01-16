from pptx import Presentation
from pptx.util import Inches, Pt
import os

def create_presentation(slides_data, image_path="drafts/images/slide_1.png"):
    prs = Presentation()

    base_dir = os.getcwd()
    abs_image_path = os.path.join(base_dir, image_path)

    print("DEBUG: image path =", abs_image_path)
    print("DEBUG: image exists =", os.path.exists(abs_image_path))

    for idx, slide_data in enumerate(slides_data):
        slide = prs.slides.add_slide(prs.slide_layouts[6])  # TRUE blank

        # -------------------------
        # IMAGE FIRST (only slide 1)
        # -------------------------
        if idx == 0 and os.path.exists(abs_image_path):
            slide.shapes.add_picture(
                abs_image_path,
                Inches(0.5),
                Inches(1.2),
                width=Inches(9)
            )
            print("DEBUG: image added to slide 1")

        # -------------------------
        # TITLE (TOP, NO OVERLAP)
        # -------------------------
        title_box = slide.shapes.add_textbox(
            Inches(0.5), Inches(0.3), Inches(9), Inches(0.8)
        )
        title_tf = title_box.text_frame
        title_tf.clear()
        title_tf.text = slide_data["title"]
        title_tf.paragraphs[0].font.size = Pt(28)
        title_tf.paragraphs[0].font.bold = True

        # -------------------------
        # TEXT CONTENT (BELOW IMAGE)
        # -------------------------
        content_box = slide.shapes.add_textbox(
            Inches(0.8), Inches(5.2), Inches(8.5), Inches(1.6)
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

    print("DEBUG: presentation saved at", output_path)
    return output_path
