"""Module for interacting with the NHL API to retrieve team-related data."""

from src.api.api_client import NHLAPIClient


class NHLTeamClient(NHLAPIClient):
    """Team Information."""

    # STANDINGS

    def get_standings(self):
        """Retrieve the standings as of the current moment."""
        endpoint = f"v1/standings/now"
        return self.get_data(endpoint)

    def get_standings_by_date(self, date: str):
        """Retrieve the standings for a specific date."""
        endpoint = f"v1/standings/{date}"
        return self.get_data(endpoint)

    # STATS

    def get_club_stats_now(self, team: str):
        """Retrieve current statistics for a specific club."""
        endpoint = f"v1/club-stats/{team}/now"
        return self.get_data(endpoint)

    # ROSTER

    def get_team_roster_as_of_now(self, team: str):
        """Retrieve the roster for a specific team as of the current moment."""
        endpoint = f"v1/roster/{team}/current"
        return self.get_data(endpoint)


# Example usage
if __name__ == "__main__":
    client = NHLTeamClient()
    result = client.get_club_stats_now("ANA")
    print(result)
