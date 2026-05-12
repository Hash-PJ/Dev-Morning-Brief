from sources.base import BaseSource


class NewsSource(BaseSource):
    TOP_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
    ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

    def fetch(self, count=3):
        """Returns list of top stories titles(strings)."""
        data = self.get(self.TOP_URL)[:count]
        if not data:
            return None
        news_list = []
        for id in data:
            params = {"id": id}
            news = self.get(self.ITEM_URL.format(id), params=params)
            news_list.append(news.get("title"))
        return news_list
