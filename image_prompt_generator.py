def generate_canva_style_prompt(title, summary):
    return f"""
Canva-style flat vector illustration for LinkedIn carousel.

Topic:
{title}

Context:
{summary}

Design style:
- Flat vector illustration
- Clean modern corporate design
- Pastel color palette
- White background
- Indian renewable energy context
- Minimal text, visual storytelling
- Icons + landscape elements
- Professional LinkedIn infographic look

Visual elements to include:
- Solar panels
- Wind turbines
- Power grid
- Green landscape
- Industrial energy infrastructure

Do NOT include text overlays.
High resolution, 16:9 aspect ratio.
"""
