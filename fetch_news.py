import feedparser

RSS_URL = (
    "https://news.google.com/rss/search?"
    "q=green+energy+OR+green+hydrogen+OR+solar+OR+renewable+OR+clean+energy"
    "&hl=en-IN&gl=IN&ceid=IN:en"
)


def fetch_news():
    feed = feedparser.parse(RSS_URL)

    news = []
    for entry in feed.entries:
        news.append({
            "title": entry.title,
            "url": entry.link,
            "source": "Google News"
        })

    return news
