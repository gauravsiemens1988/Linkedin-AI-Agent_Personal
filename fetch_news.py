import feedparser
import re

RSS_URL = (
    "https://news.google.com/rss/search?"
    "q=green+energy+OR+green+hydrogen+OR+solar+OR+renewable+OR+clean+energy"
    "&hl=en-IN&gl=IN&ceid=IN:en"
)

def clean_html(text):
    """Remove HTML tags from RSS summaries"""
    if not text:
        return ""
    return re.sub(r"<.*?>", "", text)

def fetch_news():
    feed = feedparser.parse(RSS_URL)

    news = []
    for entry in feed.entries:
        summary = ""
        if "summary" in entry:
            summary = clean_html(entry.summary)

        news.append({
            "title": entry.title,
            "url": entry.link,
            "summary": summary[:1200],  # limit length for AI
            "source": "Google News"
        })

    return news

