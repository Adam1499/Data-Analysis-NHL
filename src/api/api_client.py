import requests

class NHLAPIClient:
    BASE_URL = "https://api-web.nhle.com/"

    def __init__(self):
        self.session = requests.Session()

    def get_data(self, endpoint, params=None):
        """Generic method to get data from NHL API."""
        url = self.BASE_URL + endpoint
        response = self.session.get(url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
