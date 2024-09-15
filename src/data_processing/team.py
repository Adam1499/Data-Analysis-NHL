"""Module for processing the get_club_stats_now response."""
import pandas as pd

from src.api.team import NHLTeamClient

client = NHLTeamClient()


def filter_skaters_by_criteria(
    team: str,
    min_games: int | None = None,
    min_goals: int | None = None,
    min_assists: int | None = None,
    min_points: int | None = None,
    min_penalty_minutes: int | None = None,
) -> pd.DataFrame:
    """Filter players based on multiple criteria."""
    response = client.get_club_stats_now(team=team)
    skaters = response.get("skaters", [])
    criteria = [
        # positionCode
        lambda player: min_games is None or player.get("gamesPlayed", 0) >= min_games,
        lambda player: min_goals is None or player.get("goals", 0) >= min_goals,
        lambda player: min_assists is None or player.get("assists", 0) >= min_assists,
        lambda player: min_points is None or player.get("points", 0) >= min_points,
        # plusMinus
        lambda player: min_penalty_minutes is None
        or player.get("penaltyMinutes", 0) >= min_penalty_minutes,
        # powerPlayGoals
        # shorthandedGoals
        # overtimeGoals
        # shots
        # shootingPctg
        # avgTimeOnIcePerGame
        # faceoffWinPctg
    ]
    filtered_players = [
        player for player in skaters if all(criterion(player) for criterion in criteria)
    ]
    return filtered_players
