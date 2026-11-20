from dataclasses import dataclass
from enum import Enum
from typing import Dict, Tuple

import numpy as np
import pandas as pd


# Window sizes for rolling statistics
WINDOWS = [5, 10, 20]


class MatchResult(Enum):
    """Possible full-time match results."""
    HOME = 'H'
    DRAW = 'D'
    AWAY = 'A'


@dataclass
class WindowFeatures:
    """Features computed for a single window size (home/away stats, combined stats, strength diff)."""
    home_avg_goals: float = 0.0
    home_avg_conceded: float = 0.0
    home_win_rate: float = 0.0
    home_goal_diff: float = 0.0
    home_form: float = 0.0
    home_draw_rate: float = 0.0
    away_avg_goals: float = 0.0
    away_avg_conceded: float = 0.0
    away_win_rate: float = 0.0
    away_goal_diff: float = 0.0
    away_form: float = 0.0
    away_draw_rate: float = 0.0
    home_combined_goals: float = 0.0
    home_combined_conceded: float = 0.0
    home_combined_win: float = 0.0
    home_combined_draw: float = 0.0
    away_combined_goals: float = 0.0
    away_combined_conceded: float = 0.0
    away_combined_win: float = 0.0
    away_combined_draw: float = 0.0
    strength_diff: float = 0.0
    abs_strength_diff: float = 0.0
    goal_diff_diff: float = 0.0
    goal_similarity: float = 0.0
    combined_draw_rate: float = 0.0

    def to_dict(self, prefix: str = '') -> dict:
        """Convert to a flat dictionary with an optional key prefix."""
        return {f"{prefix}{field}": value for field, value in self.__dict__.items()}


@dataclass
class H2HFeatures:
    """Head-to-head features between two teams."""
    h2h_home_avg: float = 0.0
    h2h_away_avg: float = 0.0
    h2h_matches: int = 0
    h2h_draw_rate: float = 0.0

    def to_dict(self) -> dict:
        """Convert to a flat dictionary (no prefix — H2H features are global, not per-window)."""
        return dict(self.__dict__)


def get_team_stats(
    df: pd.DataFrame,
    team: str,
    match_date: pd.Timestamp,
    as_home: bool = True,
    window: int = 10,
) -> dict:
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


def build_window_features(
    df: pd.DataFrame,
    home_team: str,
    away_team: str,
    match_date: pd.Timestamp,
    window: int,
) -> WindowFeatures:
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

    # Combined draw rates
    home_combined_draw = (home_home_stats['draw_rate'] + home_away_stats['draw_rate']) / 2
    away_combined_draw = (away_home_stats['draw_rate'] + away_away_stats['draw_rate']) / 2

    # Combined loss rates for goal similarity
    home_combined_loss = (home_home_stats['loss_rate'] + home_away_stats['loss_rate']) / 2
    away_combined_loss = (away_home_stats['loss_rate'] + away_away_stats['loss_rate']) / 2

    # Absolute strength difference (closer to 0 = more likely draw)
    strength_diff = home_combined_win - away_combined_win
    abs_strength_diff = abs(strength_diff)

    # Goal similarity: how similar are the teams' scoring patterns?
    # Lower value = more similar = more likely draw
    home_avg_total = home_combined_goals + home_combined_conceded
    away_avg_total = away_combined_goals + away_combined_conceded
    total = home_avg_total + away_avg_total
    if total > 0:
        goal_similarity = 1.0 - abs(home_avg_total - away_avg_total) / total
    else:
        goal_similarity = 1.0

    # Combined draw rate (average of both teams' draw rates)
    combined_draw_rate = (home_combined_draw + away_combined_draw) / 2

    return WindowFeatures(
        home_avg_goals=home_home_stats['avg_goals'],
        home_avg_conceded=home_home_stats['avg_conceded'],
        home_win_rate=home_home_stats['win_rate'],
        home_goal_diff=home_home_stats['goal_diff'],
        home_form=home_home_stats['form_points'],
        home_draw_rate=home_home_stats['draw_rate'],
        away_avg_goals=away_away_stats['avg_goals'],
        away_avg_conceded=away_away_stats['avg_conceded'],
        away_win_rate=away_away_stats['win_rate'],
        away_goal_diff=away_away_stats['goal_diff'],
        away_form=away_away_stats['form_points'],
        away_draw_rate=away_away_stats['draw_rate'],
        home_combined_goals=home_combined_goals,
        home_combined_conceded=home_combined_conceded,
        home_combined_win=home_combined_win,
        home_combined_draw=home_combined_draw,
        away_combined_goals=away_combined_goals,
        away_combined_conceded=away_combined_conceded,
        away_combined_win=away_combined_win,
        away_combined_draw=away_combined_draw,
        strength_diff=strength_diff,
        abs_strength_diff=abs_strength_diff,
        goal_diff_diff=home_combined_goals - away_combined_conceded,
        goal_similarity=goal_similarity,
        combined_draw_rate=combined_draw_rate,
    )


def build_h2h_features(
    df: pd.DataFrame,
    home_team: str,
    away_team: str,
    match_date: pd.Timestamp,
) -> H2HFeatures:
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

        # H2H draw rate
        h2h_draws = (h2h['FTR'] == MatchResult.DRAW.value).sum()
        h2h_draw_rate = h2h_draws / len(h2h)

        return H2HFeatures(
            h2h_home_avg=h2h_home_goals,
            h2h_away_avg=h2h_away_goals,
            h2h_matches=len(h2h),
            h2h_draw_rate=h2h_draw_rate,
        )

    return H2HFeatures()


def build_features(
    df: pd.DataFrame,
    home_team: str,
    away_team: str,
    match_date: pd.Timestamp,
) -> dict:
    """Build all features for a single match."""
    features = {}
    for w in WINDOWS:
        window_features = build_window_features(df, home_team, away_team, match_date, w)
        features.update(window_features.to_dict(prefix=f'w{w}_'))
    h2h_features = build_h2h_features(df, home_team, away_team, match_date)
    features.update(h2h_features.to_dict())
    return features


def add_team_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add comprehensive team-based features to a DataFrame (vectorized version).
    - Rolling average goals scored/conceded at home/away
    - Win/draw/loss rates
    - Goal difference
    - Form points
    - Multiple window sizes (5, 10, 20 matches)
    - Head-to-head stats
    - Overall team strength

    Strategy: For each team, build a timeline of matches (as home and as away),
    compute rolling stats once per team per role, then use merge_asof to join
    back to the main DataFrame — avoiding the O(n²) row-by-row loop entirely.
    """
    df = df.copy()
    df['Date'] = pd.to_datetime(df['Date'], format='mixed', dayfirst=True)
    df = df.sort_values('Date').reset_index(drop=True)

    h = MatchResult.HOME.value
    d = MatchResult.DRAW.value
    a = MatchResult.AWAY.value

    # Encode results for rolling computation
    df['_is_home_win'] = (df['FTR'] == h).astype(float)
    df['_is_away_win'] = (df['FTR'] == a).astype(float)
    df['_is_draw'] = (df['FTR'] == d).astype(float)
    df['_form_points'] = df['FTR'].map({h: 3.0, d: 1.0, a: 0.0})

    # For each team, compute rolling stats as home and as away
    # We build a lookup DataFrame per (team, role) with Date as index
    team_stats: Dict[Tuple[str, str], pd.DataFrame] = {}

    all_teams = pd.concat([df['HomeTeam'], df['AwayTeam']]).unique()
    print(f"Computing features: {len(all_teams)} teams, {len(df)} matches...")

    for team in all_teams:
        for as_home in [True, False]:
            if as_home:
                mask = df['HomeTeam'] == team
                gs_col = 'FTHG'
                gc_col = 'FTAG'
                win_col = '_is_home_win'
            else:
                mask = df['AwayTeam'] == team
                gs_col = 'FTAG'
                gc_col = 'FTHG'
                win_col = '_is_away_win'

            team_df = df.loc[mask].sort_values('Date')[['Date', gs_col, gc_col, win_col, '_is_draw', '_form_points']].copy()
            team_df = team_df.dropna(subset=[gs_col])
            if len(team_df) == 0:
                role = 'home' if as_home else 'away'
                team_stats[(team, role)] = pd.DataFrame(index=pd.DatetimeIndex([]))
                continue

            # Compute rolling stats for all windows
            stats = pd.DataFrame(index=team_df['Date'])
            for w in WINDOWS:
                stats[f'g_{w}'] = team_df[gs_col].rolling(window=w, min_periods=1).mean().values
                stats[f'c_{w}'] = team_df[gc_col].rolling(window=w, min_periods=1).mean().values
                stats[f'wr_{w}'] = team_df[win_col].rolling(window=w, min_periods=1).mean().values
                stats[f'dr_{w}'] = team_df['_is_draw'].rolling(window=w, min_periods=1).mean().values
                stats[f'gd_{w}'] = (stats[f'g_{w}'] - stats[f'c_{w}']).values
                stats[f'fm_{w}'] = team_df['_form_points'].rolling(window=w, min_periods=1).mean().values

            role = 'home' if as_home else 'away'
            team_stats[(team, role)] = stats

    # Build match-level features using merge_asof (vectorized lookup)
    # For each match, we need stats for: home-as-home, home-as-away, away-as-home, away-as-away
    # merge_asof finds the last stats entry with Date < match Date

    result_dfs: Dict[str, np.ndarray] = {}

    # Prepare the match DataFrame for merging
    match_dates = df['Date'].values.copy()

    # For each (team, role) combination needed, do a merge_asof
    # We need: homeTeam-home, homeTeam-away, awayTeam-home, awayTeam-away
    # But teams vary per row, so we need to do this per unique team

    # Build a big lookup: for each team-role, create a DataFrame with match indices
    # where that team appears in that role, then merge_asof

    # More efficient: build feature arrays directly
    n = len(df)
    feature_arrays: Dict[Tuple[str, str, str], np.ndarray] = {}

    for team in all_teams:
        for role in ['home', 'away']:
            stats = team_stats.get((team, role))
            if stats is None or stats.empty:
                continue

            # Find where this team appears in this role
            if role == 'home':
                team_mask = df['HomeTeam'] == team
            else:
                team_mask = df['AwayTeam'] == team

            # For matches where this team plays in this role, look up stats
            # Use merge_asof: for each match date, find the last stats entry before it
            match_subset = pd.DataFrame({'Date': df.loc[team_mask, 'Date'].values})
            match_subset['_orig_idx'] = df.loc[team_mask].index.values

            merged = pd.merge_asof(
                match_subset.sort_values('Date'),
                stats.reset_index().rename(columns={'index': 'Date'}),
                on='Date',
                direction='backward'
            )

            for col in stats.columns:
                key = (team, role, col)
                vals = np.zeros(n)
                vals[merged['_orig_idx'].values] = merged[col].values
                feature_arrays[key] = vals

    # Now assemble features for each match
    print("Computing features: assembling match features...")
    home_teams = df['HomeTeam'].values
    away_teams = df['AwayTeam'].values

    def _get(t: str, r: str, c: str) -> np.ndarray:
        k = (t, r, c)
        return feature_arrays.get(k, np.zeros(n))

    def _extract(teams: np.ndarray, r: str, c: str) -> np.ndarray:
        """Extract a feature column for matches where each row's team plays in the given role."""
        return np.array([_get(teams[i], r, c)[i] for i in range(n)])

    def _extract_batch(teams: np.ndarray, r: str, cols: list[str]) -> Dict[str, np.ndarray]:
        """Extract multiple feature columns at once for a given team array and role."""
        return {c: _extract(teams, r, c) for c in cols}

    for w in WINDOWS:
        # Home team home stats (all 6 metrics: g, c, wr, dr, gd, fm)
        hh = _extract_batch(home_teams, 'home', [f'g_{w}', f'c_{w}', f'wr_{w}', f'dr_{w}', f'gd_{w}', f'fm_{w}'])
        hh_g, hh_c, hh_wr, hh_dr, hh_gd, hh_fm = hh[f'g_{w}'], hh[f'c_{w}'], hh[f'wr_{w}'], hh[f'dr_{w}'], hh[f'gd_{w}'], hh[f'fm_{w}']

        # Home team away stats (4 metrics: g, c, wr, dr)
        ha = _extract_batch(home_teams, 'away', [f'g_{w}', f'c_{w}', f'wr_{w}', f'dr_{w}'])
        ha_g, ha_c, ha_wr, ha_dr = ha[f'g_{w}'], ha[f'c_{w}'], ha[f'wr_{w}'], ha[f'dr_{w}']

        # Away team home stats (4 metrics: g, c, wr, dr)
        ah = _extract_batch(away_teams, 'home', [f'g_{w}', f'c_{w}', f'wr_{w}', f'dr_{w}'])
        ah_g, ah_c, ah_wr, ah_dr = ah[f'g_{w}'], ah[f'c_{w}'], ah[f'wr_{w}'], ah[f'dr_{w}']

        # Away team away stats (all 6 metrics: g, c, wr, dr, gd, fm)
        aa = _extract_batch(away_teams, 'away', [f'g_{w}', f'c_{w}', f'wr_{w}', f'dr_{w}', f'gd_{w}', f'fm_{w}'])
        aa_g, aa_c, aa_wr, aa_dr, aa_gd, aa_fm = aa[f'g_{w}'], aa[f'c_{w}'], aa[f'wr_{w}'], aa[f'dr_{w}'], aa[f'gd_{w}'], aa[f'fm_{w}']

        # Combined stats
        hc_g = (hh_g + ha_g) / 2
        hc_c = (hh_c + ha_c) / 2
        hc_wr = (hh_wr + ha_wr) / 2
        hc_dr = (hh_dr + ha_dr) / 2

        ac_g = (ah_g + aa_g) / 2
        ac_c = (ah_c + aa_c) / 2
        ac_wr = (ah_wr + aa_wr) / 2
        ac_dr = (ah_dr + aa_dr) / 2

        # Draw-specific features
        strength_diff = hc_wr - ac_wr
        abs_strength_diff = np.abs(strength_diff)

        # Goal similarity: how similar are the teams' scoring patterns?
        home_avg_total = hc_g + hc_c
        away_avg_total = ac_g + ac_c
        total = home_avg_total + away_avg_total
        goal_similarity = np.where(total > 0, 1.0 - np.abs(home_avg_total - away_avg_total) / total, 1.0)

        # Combined draw rate (average of both teams' draw rates)
        combined_draw_rate = (hc_dr + ac_dr) / 2

        # Store as DataFrame columns
        prefix = f'w{w}_'
        for key, value in {
            'home_avg_goals': hh_g,
            'home_avg_conceded': hh_c,
            'home_win_rate': hh_wr,
            'home_goal_diff': hh_gd,
            'home_form': hh_fm,
            'home_draw_rate': hh_dr,
            'away_avg_goals': aa_g,
            'away_avg_conceded': aa_c,
            'away_win_rate': aa_wr,
            'away_goal_diff': aa_gd,
            'away_form': aa_fm,
            'away_draw_rate': aa_dr,
            'home_combined_goals': hc_g,
            'home_combined_conceded': hc_c,
            'home_combined_win': hc_wr,
            'home_combined_draw': hc_dr,
            'away_combined_goals': ac_g,
            'away_combined_conceded': ac_c,
            'away_combined_win': ac_wr,
            'away_combined_draw': ac_dr,
            'strength_diff': strength_diff,
            'abs_strength_diff': abs_strength_diff,
            'goal_diff_diff': hc_g - ac_c,
            'goal_similarity': goal_similarity,
            'combined_draw_rate': combined_draw_rate,
        }.items():
            result_dfs[f'{prefix}{key}'] = value

    # H2H features — vectorized approach using groupby + rolling
    print("Computing features: head-to-head stats...")
    h2h_home_avg = np.zeros(n)
    h2h_away_avg = np.zeros(n)
    h2h_matches_arr = np.zeros(n, dtype=int)
    h2h_draw_rate_arr = np.zeros(n)

    # Build a DataFrame of all H2H matches with pair key
    df_h2h = df.copy()
    # Create a canonical pair key (sorted team names) for grouping
    df_h2h['_pair'] = df_h2h.apply(
        lambda r: tuple(sorted([r['HomeTeam'], r['AwayTeam']])), axis=1
    )

    # Process each unique pair
    for _pair, group in df_h2h.groupby('_pair'):
        group = group.sort_values('Date').reset_index(drop=True)
        g_len = len(group)
        if g_len == 0:
            continue

        # For each match in the group, compute H2H stats from previous matches
        # Use cumulative approach: for each row, look at the last 5 previous rows
        dates = group['Date'].values
        orig_indices = group.index.values  # original df indices

        # For each match, the "home" team in the pair context
        # We need to track which team scored what from the perspective of
        # the original match's home team
        home_teams_in_group = group['HomeTeam'].values
        away_teams_in_group = group['AwayTeam'].values
        flag_vals = group['FTHG'].values
        ftag_vals = group['FTAG'].values

        for j in range(g_len):
            md = dates[j]
            orig_idx = orig_indices[j]
            # Find matches before this date
            before_mask = dates[:j] < md
            before_indices = np.where(before_mask)[0]
            if len(before_indices) == 0:
                continue
            # Take last 5
            last5 = before_indices[-5:]

            # The home team for this match
            ht = home_teams_in_group[j]
            at = away_teams_in_group[j]

            # For each of the last 5 H2H matches, get goals from ht and at perspective
            ht_goals = []
            at_goals = []
            for k in last5:
                if home_teams_in_group[k] == ht:
                    ht_goals.append(flag_vals[k])
                    at_goals.append(ftag_vals[k])
                else:
                    ht_goals.append(ftag_vals[k])
                    at_goals.append(flag_vals[k])

            h2h_home_avg[orig_idx] = float(np.mean(ht_goals)) if ht_goals else 0.0
            h2h_away_avg[orig_idx] = float(np.mean(at_goals)) if at_goals else 0.0
            h2h_matches_arr[orig_idx] = len(last5)
            # H2H draw rate
            if len(last5) > 0:
                ftr_before = group['FTR'].values[last5]
                h2h_draw_rate_arr[orig_idx] = float(np.sum(ftr_before == d)) / len(last5)

    result_dfs['h2h_home_avg'] = h2h_home_avg
    result_dfs['h2h_away_avg'] = h2h_away_avg
    result_dfs['h2h_matches'] = h2h_matches_arr
    result_dfs['h2h_draw_rate'] = h2h_draw_rate_arr

    # Join all features
    features_df = pd.DataFrame(result_dfs, index=df.index)
    df = df.join(features_df)

    # Clean up temporary columns
    df.drop(columns=['_is_home_win', '_is_away_win', '_is_draw', '_form_points'], inplace=True)

    return df
