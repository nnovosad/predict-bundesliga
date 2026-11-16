from dataclasses import dataclass
from enum import Enum
import pandas as pd
from tqdm import tqdm


# Window sizes for rolling statistics
WINDOWS = [5, 10, 20]


class MatchResult(Enum):
    """Possible full-time match results."""
    HOME = 'H'
    DRAW = 'D'
    AWAY = 'A'


@dataclass
class MatchFeatures:
    """Aggregates all computed features for a single match window into one typed object."""
    home_avg_goals: float = 0.0
    home_avg_conceded: float = 0.0
    home_win_rate: float = 0.0
    home_goal_diff: float = 0.0
    home_form: float = 0.0
    away_avg_goals: float = 0.0
    away_avg_conceded: float = 0.0
    away_win_rate: float = 0.0
    away_goal_diff: float = 0.0
    away_form: float = 0.0
    home_combined_goals: float = 0.0
    home_combined_conceded: float = 0.0
    home_combined_win: float = 0.0
    away_combined_goals: float = 0.0
    away_combined_conceded: float = 0.0
    away_combined_win: float = 0.0
    strength_diff: float = 0.0
    goal_diff_diff: float = 0.0
    h2h_home_avg: float = 0.0
    h2h_away_avg: float = 0.0
    h2h_matches: int = 0

    def to_dict(self, prefix: str = '') -> dict:
        """Convert to a flat dictionary with an optional key prefix."""
        return {f"{prefix}{field}": value for field, value in self.__dict__.items()}


def get_team_stats(df, team, match_date, as_home=True, window=10):
    """Get statistics for a team within a time window before a match."""
    if as_home:
        history = df[
            (df['HomeTeam'] == team) &
            (df['Date'] < match_date)
        ].tail(window)
    else:
        history = df[
            (df['AwayTeam'] == team) &
            (df['Date'] < match_date)
        ].tail(window)

    if len(history) == 0:
        return {
            'avg_goals': 0,
            'avg_conceded': 0,
            'win_rate': 0,
            'draw_rate': 0,
            'loss_rate': 0,
            'goal_diff': 0,
            'form_points': 0,
            'matches_played': 0,
        }

    if as_home:
        goals_scored = history['FTHG']
        goals_conceded = history['FTAG']
        wins = (history['FTR'] == MatchResult.HOME.value).sum()
        draws = (history['FTR'] == MatchResult.DRAW.value).sum()
        losses = (history['FTR'] == MatchResult.AWAY.value).sum()
    else:
        goals_scored = history['FTAG']
        goals_conceded = history['FTHG']
        wins = (history['FTR'] == MatchResult.AWAY.value).sum()
        draws = (history['FTR'] == MatchResult.DRAW.value).sum()
        losses = (history['FTR'] == MatchResult.HOME.value).sum()

    n = len(history)
    return {
        'avg_goals': goals_scored.mean(),
        'avg_conceded': goals_conceded.mean(),
        'win_rate': wins / n,
        'draw_rate': draws / n,
        'loss_rate': losses / n,
        'goal_diff': (goals_scored - goals_conceded).mean(),
        'form_points': history['FTR'].map({
            MatchResult.HOME.value: 3,
            MatchResult.DRAW.value: 1,
            MatchResult.AWAY.value: 0,
        }).mean(),
        'matches_played': n,
    }


def build_window_features(df, home_team, away_team, match_date, window):
    """Build features for a single window size."""
    # Home team as home
    home_home_stats = get_team_stats(df, home_team, match_date, as_home=True, window=window)
    # Home team as away
    home_away_stats = get_team_stats(df, home_team, match_date, as_home=False, window=window)
    # Away team as home
    away_home_stats = get_team_stats(df, away_team, match_date, as_home=True, window=window)
    # Away team as away
    away_away_stats = get_team_stats(df, away_team, match_date, as_home=False, window=window)

    # Combined home team stats (home + away matches)
    home_combined_goals = (home_home_stats['avg_goals'] + home_away_stats['avg_goals']) / 2
    home_combined_conceded = (home_home_stats['avg_conceded'] + home_away_stats['avg_conceded']) / 2
    home_combined_win = (home_home_stats['win_rate'] + home_away_stats['win_rate']) / 2

    # Combined away team stats
    away_combined_goals = (away_home_stats['avg_goals'] + away_away_stats['avg_goals']) / 2
    away_combined_conceded = (away_home_stats['avg_conceded'] + away_away_stats['avg_conceded']) / 2
    away_combined_win = (away_home_stats['win_rate'] + away_away_stats['win_rate']) / 2

    return MatchFeatures(
        home_avg_goals=home_home_stats['avg_goals'],
        home_avg_conceded=home_home_stats['avg_conceded'],
        home_win_rate=home_home_stats['win_rate'],
        home_goal_diff=home_home_stats['goal_diff'],
        home_form=home_home_stats['form_points'],
        away_avg_goals=away_away_stats['avg_goals'],
        away_avg_conceded=away_away_stats['avg_conceded'],
        away_win_rate=away_away_stats['win_rate'],
        away_goal_diff=away_away_stats['goal_diff'],
        away_form=away_away_stats['form_points'],
        home_combined_goals=home_combined_goals,
        home_combined_conceded=home_combined_conceded,
        home_combined_win=home_combined_win,
        away_combined_goals=away_combined_goals,
        away_combined_conceded=away_combined_conceded,
        away_combined_win=away_combined_win,
        strength_diff=home_combined_win - away_combined_win,
        goal_diff_diff=home_combined_goals - away_combined_conceded,
    )


def build_h2h_features(df, home_team, away_team, match_date):
    """Build head-to-head features."""
    h2h = df[
        ((df['HomeTeam'] == home_team) & (df['AwayTeam'] == away_team)) |
        ((df['HomeTeam'] == away_team) & (df['AwayTeam'] == home_team))
    ]
    h2h = h2h[h2h['Date'] < match_date].tail(5)

    if len(h2h) > 0:
        h2h_home_matches = h2h[h2h['HomeTeam'] == home_team]
        h2h_away_matches = h2h[h2h['HomeTeam'] == away_team]

        h2h_home_goals = 0
        if len(h2h_home_matches) > 0:
            h2h_home_goals = h2h_home_matches['FTHG'].mean()
        elif len(h2h_away_matches) > 0:
            h2h_home_goals = h2h_away_matches['FTAG'].mean()

        h2h_away_goals = 0
        if len(h2h_away_matches) > 0:
            h2h_away_goals = h2h_away_matches['FTAG'].mean()
        elif len(h2h_home_matches) > 0:
            h2h_away_goals = h2h_home_matches['FTHG'].mean()

        return MatchFeatures(
            h2h_home_avg=h2h_home_goals,
            h2h_away_avg=h2h_away_goals,
            h2h_matches=len(h2h),
        )

    return MatchFeatures()


def build_features(df, home_team, away_team, match_date):
    """Build all features for a single match."""
    features = {}
    for w in WINDOWS:
        window_features = build_window_features(df, home_team, away_team, match_date, w)
        features.update(window_features.to_dict(prefix=f'w{w}_'))
    h2h_features = build_h2h_features(df, home_team, away_team, match_date)
    features.update(h2h_features.to_dict())
    return features


def add_team_features(df):
    """
    Add comprehensive team-based features to a DataFrame:
    - Rolling average goals scored/conceded at home/away
    - Win/draw/loss rates
    - Goal difference
    - Form points
    - Multiple window sizes (5, 10, 20 matches)
    - Head-to-head stats
    - Overall team strength
    """
    df = df.copy()
    df['Date'] = pd.to_datetime(df['Date'], format='mixed', dayfirst=True)
    df = df.sort_values('Date').reset_index(drop=True)

    feature_lists = {}

    for idx, row in tqdm(df.iterrows(), total=len(df), desc="Computing features"):
        home_team = row['HomeTeam']
        away_team = row['AwayTeam']
        match_date = row['Date']

        features = build_features(df, home_team, away_team, match_date)

        feature_lists[idx] = features

    # Convert feature lists to dataframe
    features_df = pd.DataFrame.from_records(list(feature_lists.values()), index=list(feature_lists.keys()))
    df = df.join(features_df)

    return df
