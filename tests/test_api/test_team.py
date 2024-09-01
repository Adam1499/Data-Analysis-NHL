import unittest
from unittest.mock import patch
from src.api.api_client import NHLAPIClient
from src.api.team import NHLTeamClient

class NHLTeamClientTestCase(unittest.TestCase):
    def setUp(self):
        self.client = NHLTeamClient()
    
    @patch.object(NHLAPIClient, 'get_data')
    def test_get_standings(self, mock_get_data):
        # Define the mock response
        mock_response = {"standings": "mock_standings_data"}
        mock_get_data.return_value = mock_response
        
        # Call the method
        result = self.client.get_standings()
        
        # Assertions
        mock_get_data.assert_called_once_with("v1/standings/now")
        self.assertEqual(result, mock_response)
    
    @patch.object(NHLAPIClient, 'get_data')
    def test_get_standings_by_date(self, mock_get_data):
        # Define the mock response
        mock_response = {"standings": "mock_standings_data_by_date"}
        date = "2023-11-10"
        mock_get_data.return_value = mock_response
        
        # Call the method
        result = self.client.get_standings_by_date(date)
        
        # Assertions
        mock_get_data.assert_called_once_with(f"v1/standings/{date}")
        self.assertEqual(result, mock_response)

if __name__ == "__main__":
    unittest.main()