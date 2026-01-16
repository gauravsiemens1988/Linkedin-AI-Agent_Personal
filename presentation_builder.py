from pptx import Presentation
from pptx.util import Inches, Pt
import os

def create_presentation(slides_data, image_folder="drafts/images"):
    prs = Presentation()
    base_dir = os.getcwd()

    for idx, slide_data in enumerate(slides_data, start=1):
        slide = prs.slides.add_slide(prs.slide_layouts[6])  # blank slide

        # ----------------------------------
        # Resolve image path for this slide
        # ----------------------------------
        image_name = f"slide_{idx}.png"
        image_path = os.path.join(base_dir, image_folder, image_name)

        print(f"DEBUG: Slide {idx} image path =", image_path)
        print(f"DEBUG: Exists =", os.path.exists(image_path))

        # ----------------------------------
        # Insert image IF available
        # ----------------------------------
        if os.path.exists(image_path):
            slide.shapes.add_picture(
                image_path,
                Inches(0.5),
                Inches(1.2),
                width=Inches(9)
            )
            print(f"DEBUG: Image added on slide {idx}")

        # ----------------------------------
        # Title
        # ----------------------------------
        title_box = slide.shapes.add_textbox(
            Inches(0.5), Inches(0.3), Inches(9), Inches(0.8)
        )
        title_tf = title_box.text_frame
        title_tf.clear()
        title_tf.text = slide_data["title"]
        title_tf.paragraphs[0].font.size = Pt(28)
        title_tf.paragraphs[0].font.bold = True

        # ----------------------------------
        # Text content
        # ----------------------------------
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

    print("DEBUG: Presentation saved at", output_path)
    return output_path

