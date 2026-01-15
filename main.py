from fetch_news import fetch_news

print("🚀 LinkedIn AI Agent started")

news = fetch_news()

print(f"📰 Fetched {len(news)} news items")

if news:
    print("Sample news title:")
    print(news[0]["title"])




