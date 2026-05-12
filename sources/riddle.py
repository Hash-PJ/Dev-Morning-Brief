from sources.base import BaseSource


class RiddleSource(BaseSource):
    URL = "https://riddles-api.vercel.app/random"
    
    def fetch(self):
        data = self.get(self.URL)
        if not data:
            return None
        return data
