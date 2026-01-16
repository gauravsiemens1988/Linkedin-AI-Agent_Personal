import feedparser
from image_prompt_generator import generate_canva_style_prompt
from image_generator import generate_image
from presentation_builder import create_presentation

print("🚀 LinkedIn AI Agent started")

# ---------------------------------------
# Fetch latest green energy news
# ---------------------------------------
RSS_URL = (
    "https://news.google.com/rss/search?"
    "q=green+energy+OR+solar+OR+wind+OR+hydrogen+OR+renewable"
    "&hl=en-IN&gl=IN&ceid=IN:en"
)

feed = feedparser.parse(RSS_URL)
article = feed.entries[0]

title = article.title
summary = article.get("summary", title)
link = article.link

print("🟢 Selected article:")
print(title)

# ---------------------------------------
# Generate image prompt (semi-auto)
# ---------------------------------------
prompt = generate_canva_style_prompt(title, summary)
generate_image(prompt)

# ---------------------------------------
# Build LinkedIn carousel slides
# ---------------------------------------
slides_data = [
    {
        "title": title,
        "points": [
            "Strategic joint venture in India’s clean energy sector"
        ]
    },
    {
        "title": "Key Highlights",
        "points": [
            "NTPC Green Energy approves a 50:50 JV with GAIL",
            "Focus on renewable and clean energy projects",
            "Strengthens public-sector collaboration"
        ]
    },
    {
        "title": "Why This Matters",
        "points": [
            "Accelerates India’s energy transition",
            "Supports green hydrogen and renewables",
            "Enhances long-term energy security"
        ]
    },
    {
        "title": "Industry Impact",
        "points": [
            "Boosts investor confidence in green energy",
            "Encourages large-scale clean infrastructure",
            "Aligns with India’s net-zero goals"
        ]
    },
    {
        "title": "Source",
        "points": [
            "India Infoline",
            "Read full article online"
        ]
    }
]

# ---------------------------------------
# Create presentation
# ---------------------------------------
pptx_path = create_presentation(slides_data)

print(f"📊 Presentation generated: {pptx_path}")
print("✅ LinkedIn AI Agent finished successfully")



