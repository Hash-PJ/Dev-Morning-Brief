from sources.base import BaseSource


class JokeSource(BaseSource):
    URL = "https://v2.jokeapi.dev/joke/programming"

    def fetch(self):
        """Returns Joke as a string"""
        data = self.get(self.URL)
        if not data:
            return None
        if data.get('type') == 'single':
            return data.get('joke')
        if data.get('type')=='twopart':
            return data.get('setup')+'\n'+data.get('delivery')
