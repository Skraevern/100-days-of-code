import os
import requests

API = "https://newsapi.org/v2/everything"  # ?q=tesla&from=2023-09-10&sortBy=publishedAt&apiKey=
PARAMETERS = {
    "q": "tesla",
    "from": "2023-09-10",
    "sortBy": "publishedAt",
    "apiKey": os.environ.get("NEWSAPIDOTORG_KEY"),
    "language": "en",
}


class NewsHandler:
    def __init__(self) -> None:
        self.response = requests.get(url=API, params=PARAMETERS)
        self.response.raise_for_status()
        self.data = self.response.json()

    def get_3_articles(self, new_stock, old_stock, percentage):
        articles = (
            f"TSLA: {new_stock}\n"
            f'{"🔺" if percentage > 0 else "🔻"}'
            f"{round(percentage, 2)}% from {old_stock}\n"
        )
        for i in range(0, 3):
            articles += (
                f'Headline: {self.data["articles"][i]["title"]}\n'
                f'Brief: {self.data["articles"][i]["description"]}\n\n'
            )
        return articles
