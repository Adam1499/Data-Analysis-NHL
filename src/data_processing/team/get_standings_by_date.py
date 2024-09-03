"""Module for processing the get_standings_by_date response."""

from pathlib import Path
import requests


def download_all_team_logos(stats_data) -> None:
    """Downloads all team logos from the standings data and saves them."""
    for team in stats_data["standings"]:
        team_logo_url = team["teamLogo"]
        team_name = team["teamName"]["default"]
        file_name = Path("data/team_logos", f"{team_name}.svg")
        response = requests.get(team_logo_url)
        with open(file_name, "wb") as f:
            f.write(response.content)
