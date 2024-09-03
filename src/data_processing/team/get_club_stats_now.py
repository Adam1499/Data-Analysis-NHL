"""Module for processing the get_club_stats_now response."""


def filter_skaters_by_criteria(
    stats_data,
    min_games=None,
    min_goals=None,
    min_assists=None,
    min_points=None,
    min_penalty_minutes=None,
):
    """Filter players based on multiple criteria."""
    skaters = stats_data.get("skaters", [])
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
