import requests

API_KEY = "64e88452f8184cb1996a62f27332b11b"

def get_news(topic):

    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={API_KEY}"

    response = requests.get(url)

    data = response.json()

    print(f"\n===== {topic.upper()} NEWS =====")

    for article in data["articles"][:5]:
        print("-", article["title"])

get_news("technology")
get_news("artificial intelligence")