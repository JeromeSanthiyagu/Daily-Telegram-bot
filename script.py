import os
import requests
from datetime import datetime
import random

# === CONFIG ===
BOT_TOKEN = "8379036999:AAGX2bAndGre0Z4nc1ysE79-XXU5tK2-ZFg"
USER_ID = "1702396189"
NEWS_API_KEY = "1576948dc78a4edb8441d1d189a6517a"

# === 1. Fetch Tech News ===
def get_tech_news():
    url = f"https://newsapi.org/v2/top-headlines?country=in&category=technology&pageSize=5&apiKey={NEWS_API_KEY}"
    res = requests.get(url).json()
    articles = res.get("articles", [])
    headlines = ""
    for i, article in enumerate(articles):
        title = article['title']
        url = article['url']
        headlines += f"{i+1}. {title}\n🔗 {url}\n\n"
    return headlines

# === 2. GD Topics ===
def get_gd_topics():
    topics = [
        "Impact of AI on Traditional Jobs",
        "Remote Work: Future of IT or Just a Trend?",
        "Digital India – Real Progress or Just Buzz?",
        "Green Tech – Can India Lead?",
        "Should coding be taught in all schools?"
    ]
    return "\n".join([f"• {t}" for t in topics])

# === 3. Send Message to Telegram ===
def send_daily_update():
    today = datetime.now().strftime("%d %B %Y")
    tech_news = get_tech_news()
    gd = get_gd_topics()

    message = f"🧠 *Your Daily Tech + GD Brief* - _{today}_\n\n"
    message += "*📰 Top Tech News:*\n" + tech_news
    message += "*💬 GD Topics:*\n" + gd

    payload = {
        "chat_id": USER_ID,
        "text": message,
        "parse_mode": "Markdown"
    }

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        print("✅ Message sent successfully!")
    else:
        print("❌ Failed to send:", response.text)

# Run it
send_daily_update()
