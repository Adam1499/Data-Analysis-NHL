"""Module for interacting with the NHL API to retrieve player-related data."""

from src.api.api_client import NHLAPIClient


class NHLPlayerClient(NHLAPIClient):
    """Player Information."""

    def get_current_skater_stats_leaders(self):
        """Retrieve current skater stats leaders."""
        endpoint = f"v1/skater-stats-leaders/current"
        return self.get_data(endpoint)


# Example usage
if __name__ == "__main__":
    client = NHLPlayerClient()
    standings = client.get_current_skater_stats_leaders()
    print(standings)
