import requests

class BaseSource:
    """Every source inherits from this class"""
    TIMEOUT = 5
    def fetch(self):
        raise NotImplementedError("Every source must implement fetch()")

    def get(self, url, params=None, headers=None):
        """Shared GET helper with error handling"""
        try:
            response = requests.get(
                url,
                params=params,
                headers=headers,
                timeout=self.TIMEOUT)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.ConnectionError:
            print(f"[{self.__class__.__name__}] No internet connection!")
        except requests.exceptions.Timeout:
            print(f"[{self.__class__.__name__}] Request timed out!")
        except requests.exceptions.HTTPError as e:
            print(f"[{self.__class__.__name__}] HTTP error: {e}")
        return None
