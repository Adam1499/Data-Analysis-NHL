"""Module for interacting with the NHL API using HTTP requests."""

import requests


class NHLAPIClient:
    """A base client for making HTTP requests to the NHL API."""

    BASE_URL = "https://api-web.nhle.com/"

    def __init__(self):
        """Initializes the NHLAPIClient with a requests session.

        This constructor creates a persistent HTTP session for the client,
        which allows for more efficient reuse of connections when making
        multiple requests to the NHL API.
        """
        self.session = requests.Session()

    def get_data(self, endpoint, params=None):
        """Retrieves data from the NHL API for a given endpoint.

        This method constructs the full URL by combining the base URL and the
        endpoint provided, then makes a GET request to the NHL API. If the
        request is successful, the method returns the JSON response. In case
        of an HTTP error, an exception is raised.

        Args:
            endpoint (str): The API endpoint to request data from, e.g., 'v1/standings/now'.
            params (dict, optional): A dictionary of query parameters to include in the request.

        Returns:
            dict: The JSON data returned by the NHL API.

        Raises:
            requests.exceptions.HTTPError: If the HTTP request returned an unsuccessful status code.
        """
        url = self.BASE_URL + endpoint
        response = self.session.get(url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
