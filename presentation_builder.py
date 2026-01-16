from pptx import Presentation
from pptx.util import Inches, Pt
import os

def create_presentation(
    slides_data,
    image_folder="drafts/images",
):
    prs = Presentation()
    layout = prs.slide_layouts[1]  # Title + Content (stable)

    base_dir = os.getcwd()
    image_folder_path = os.path.join(base_dir, image_folder)

    print("DEBUG: image_folder_path =", image_folder_path)

    image_path = None
    if os.path.exists(image_folder_path):
        for f in sorted(os.listdir(image_folder_path)):
            if f.lower().endswith(".png"):
                image_path = os.path.join(image_folder_path, f)
                break

    print("DEBUG: resolved image_path =", image_path)

    for slide_data in slides_data:
        slide = prs.slides.add_slide(layout)

        # ---------- TITLE ----------
        title = slide.shapes.title
        short_title = slide_data["title"].split(" - ")[0][:60]
        title.text = short_title
        title.text_frame.paragraphs[0].font.size = Pt(32)
        title.text_frame.paragraphs[0].font.bold = True

        # ---------- CONTENT ----------
        content = slide.placeholders[1]
        tf = content.text_frame
        tf.clear()

        # ---------- IMAGE ----------
        if image_path and os.path.exists(image_path):
            slide.shapes.add_picture(
                image_path,
                Inches(1),
                Inches(2),
                width=prs.slide_width - Inches(2),
                height=Inches(3.5)
            )
        else:
            tf.text = "Image will appear here (add slide_1.png)"

        # ---------- BULLETS ----------
        for point in slide_data["points"][:3]:
            p = tf.add_paragraph()
            p.text = point
            p.font.size = Pt(16)
            p.level = 1

    os.makedirs("drafts", exist_ok=True)
    output_path = "drafts/linkedin_carousel.pptx"
    prs.save(output_path)

    print("DEBUG: PPT saved at", output_path)
    return output_path




