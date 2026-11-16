import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from tqdm import tqdm

import results as rs
import match_days as md

from random import randrange

def read_and_concat_files(directory):
    fnames = []
    for dirname, _, filenames in os.walk(directory):
        for filename in filenames:
            try:
                pd.read_csv(os.path.join(dirname, filename))
                fnames.append(os.path.join(dirname, filename))
            except Exception as e:
                continue
    return pd.concat((pd.read_csv(f) for f in tqdm(fnames)), ignore_index=True)


def load_results_dataframes():
    return [rs.results_d1, rs.results_d2, rs.results_d3, rs.results_d4, rs.results_d5, rs.results_d6, rs.results_d7,
            rs.results_d8, rs.results_d9]


def preprocess_dataframe(df):
    columns_to_keep = ["FTHG", "HTHG", "FTAG", "HTAG", "FTR", "HTR", "HomeTeam", "AwayTeam", "Date"]
    return df[columns_to_keep]


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
        wins = (history['FTR'] == 'H').sum()
        draws = (history['FTR'] == 'D').sum()
        losses = (history['FTR'] == 'A').sum()
    else:
        goals_scored = history['FTAG']
        goals_conceded = history['FTHG']
        wins = (history['FTR'] == 'A').sum()
        draws = (history['FTR'] == 'D').sum()
        losses = (history['FTR'] == 'H').sum()
    
    n = len(history)
    return {
        'avg_goals': goals_scored.mean(),
        'avg_conceded': goals_conceded.mean(),
        'win_rate': wins / n,
        'draw_rate': draws / n,
        'loss_rate': losses / n,
        'goal_diff': (goals_scored - goals_conceded).mean(),
        'form_points': history['FTR'].map({'H': 3, 'D': 1, 'A': 0}).mean(),
        'matches_played': n,
    }


def add_team_features(df):
    """
    Add comprehensive team-based features:
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
    
    windows = [5, 10, 20]
    
    # Pre-compute team indices for faster lookup
    teams = df['HomeTeam'].unique()
    
    feature_lists = {}
    
    for idx, row in tqdm(df.iterrows(), total=len(df), desc="Computing features"):
        home_team = row['HomeTeam']
        away_team = row['AwayTeam']
        match_date = row['Date']
        
        features = {}
        
        # Features for each window size
        for w in windows:
            # Home team as home
            home_home_stats = get_team_stats(df, home_team, match_date, as_home=True, window=w)
            # Home team as away
            home_away_stats = get_team_stats(df, home_team, match_date, as_home=False, window=w)
            # Away team as home
            away_home_stats = get_team_stats(df, away_team, match_date, as_home=True, window=w)
            # Away team as away
            away_away_stats = get_team_stats(df, away_team, match_date, as_home=False, window=w)
            
            # Combined home team stats (home + away matches)
            home_combined_goals = (home_home_stats['avg_goals'] + home_away_stats['avg_goals']) / 2
            home_combined_conceded = (home_home_stats['avg_conceded'] + home_away_stats['avg_conceded']) / 2
            home_combined_win = (home_home_stats['win_rate'] + home_away_stats['win_rate']) / 2
            
            # Combined away team stats
            away_combined_goals = (away_home_stats['avg_goals'] + away_away_stats['avg_goals']) / 2
            away_combined_conceded = (away_home_stats['avg_conceded'] + away_away_stats['avg_conceded']) / 2
            away_combined_win = (away_home_stats['win_rate'] + away_away_stats['win_rate']) / 2
            
            prefix = f'w{w}'
            features[f'{prefix}_home_avg_goals'] = home_home_stats['avg_goals']
            features[f'{prefix}_home_avg_conceded'] = home_home_stats['avg_conceded']
            features[f'{prefix}_home_win_rate'] = home_home_stats['win_rate']
            features[f'{prefix}_home_goal_diff'] = home_home_stats['goal_diff']
            features[f'{prefix}_home_form'] = home_home_stats['form_points']
            
            features[f'{prefix}_away_avg_goals'] = away_away_stats['avg_goals']
            features[f'{prefix}_away_avg_conceded'] = away_away_stats['avg_conceded']
            features[f'{prefix}_away_win_rate'] = away_away_stats['win_rate']
            features[f'{prefix}_away_goal_diff'] = away_away_stats['goal_diff']
            features[f'{prefix}_away_form'] = away_away_stats['form_points']
            
            features[f'{prefix}_home_combined_goals'] = home_combined_goals
            features[f'{prefix}_home_combined_conceded'] = home_combined_conceded
            features[f'{prefix}_home_combined_win'] = home_combined_win
            
            features[f'{prefix}_away_combined_goals'] = away_combined_goals
            features[f'{prefix}_away_combined_conceded'] = away_combined_conceded
            features[f'{prefix}_away_combined_win'] = away_combined_win
            
            # Strength difference
            features[f'{prefix}_strength_diff'] = home_combined_win - away_combined_win
            features[f'{prefix}_goal_diff_diff'] = home_combined_goals - away_combined_conceded
            
        # Head-to-head
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
            
            features['h2h_home_avg'] = h2h_home_goals
            features['h2h_away_avg'] = h2h_away_goals
            features['h2h_matches'] = len(h2h)
        else:
            features['h2h_home_avg'] = 0
            features['h2h_away_avg'] = 0
            features['h2h_matches'] = 0
        
        feature_lists[idx] = features
    
    # Convert feature lists to dataframe
    features_df = pd.DataFrame.from_records(list(feature_lists.values()), index=list(feature_lists.keys()))
    df = df.join(features_df)
    
    return df


def train_predict_rf(X_train, y_train, X_test):
    rf = RandomForestClassifier(n_estimators=1000, random_state=41, n_jobs=-1)
    rf.fit(X_train, y_train)
    predictions = rf.predict(X_test)
    return predictions


def evaluate_model(y_true, y_pred):
    acc = accuracy_score(y_true, y_pred)
    report = classification_report(y_true, y_pred, target_names=['Home Win (H)', 'Draw (D)', 'Away Win (A)'])
    return acc, report


def predict_result(home_team, away_team, label_encoders, model, df_full, feature_cols):
    """Predict match result (H/D/A) with probabilities for a specific match."""
    home_team_encoded = label_encoders['HomeTeam'].transform([home_team])
    away_team_encoded = label_encoders['AwayTeam'].transform([away_team])
    
    max_date = df_full['Date'].max()
    windows = [5, 10, 20]
    
    features = {
        'HomeTeam': [home_team_encoded[0]],
        'AwayTeam': [away_team_encoded[0]]
    }
    
    for w in windows:
        # Home team as home
        hh = get_team_stats(df_full, home_team, max_date, as_home=True, window=w)
        # Home team as away  
        ha = get_team_stats(df_full, home_team, max_date, as_home=False, window=w)
        # Away team as home
        ah = get_team_stats(df_full, away_team, max_date, as_home=True, window=w)
        # Away team as away
        aa = get_team_stats(df_full, away_team, max_date, as_home=False, window=w)
        
        home_combined_goals = (hh['avg_goals'] + ha['avg_goals']) / 2
        home_combined_conceded = (hh['avg_conceded'] + ha['avg_conceded']) / 2
        home_combined_win = (hh['win_rate'] + ha['win_rate']) / 2
        
        away_combined_goals = (ah['avg_goals'] + aa['avg_goals']) / 2
        away_combined_conceded = (ah['avg_conceded'] + aa['avg_conceded']) / 2
        away_combined_win = (ah['win_rate'] + aa['win_rate']) / 2
        
        prefix = f'w{w}'
        features[f'{prefix}_home_avg_goals'] = [hh['avg_goals']]
        features[f'{prefix}_home_avg_conceded'] = [hh['avg_conceded']]
        features[f'{prefix}_home_win_rate'] = [hh['win_rate']]
        features[f'{prefix}_home_goal_diff'] = [hh['goal_diff']]
        features[f'{prefix}_home_form'] = [hh['form_points']]
        
        features[f'{prefix}_away_avg_goals'] = [aa['avg_goals']]
        features[f'{prefix}_away_avg_conceded'] = [aa['avg_conceded']]
        features[f'{prefix}_away_win_rate'] = [aa['win_rate']]
        features[f'{prefix}_away_goal_diff'] = [aa['goal_diff']]
        features[f'{prefix}_away_form'] = [aa['form_points']]
        
        features[f'{prefix}_home_combined_goals'] = [home_combined_goals]
        features[f'{prefix}_home_combined_conceded'] = [home_combined_conceded]
        features[f'{prefix}_home_combined_win'] = [home_combined_win]
        
        features[f'{prefix}_away_combined_goals'] = [away_combined_goals]
        features[f'{prefix}_away_combined_conceded'] = [away_combined_conceded]
        features[f'{prefix}_away_combined_win'] = [away_combined_win]
        
        features[f'{prefix}_strength_diff'] = [home_combined_win - away_combined_win]
        features[f'{prefix}_goal_diff_diff'] = [home_combined_goals - away_combined_conceded]
    
    # Head-to-head
    h2h = df_full[
        ((df_full['HomeTeam'] == home_team) & (df_full['AwayTeam'] == away_team)) |
        ((df_full['HomeTeam'] == away_team) & (df_full['AwayTeam'] == home_team))
    ].tail(5)
    
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
        
        features['h2h_home_avg'] = [h2h_home_goals]
        features['h2h_away_avg'] = [h2h_away_goals]
        features['h2h_matches'] = [len(h2h)]
    else:
        features['h2h_home_avg'] = [0]
        features['h2h_away_avg'] = [0]
        features['h2h_matches'] = [0]
    
    prediction_input = pd.DataFrame(features)[feature_cols]
    prediction = model.predict(prediction_input)
    probabilities = model.predict_proba(prediction_input)
    return prediction[0], probabilities[0]


def main():
    kaggle_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'kaggle', 'input')
    df = read_and_concat_files(kaggle_path)

    # FTHG: Full Time Home Team Goals
    # HTHG: Half Time Home Team Goals
    # FTAG: Full Time Away Team Goals
    # HTAG: Half Time Away Team Goals
    # FTR: Full Time Result (being either "H", "A" or "D" for "Draw")
    # HTR: Half Time Result (being either "H", "A" or "D" for "Draw")
    # HomeTeam: Name of the home team
    # AwayTeam: Name of the away team

    print(df[["FTHG", "HTHG", "FTAG", "HTAG", "FTR", "HTR"]].describe())
    print(df[["FTHG", "HTHG", "FTAG", "HTAG", "FTR", "HTR"]].isnull().sum())

    results_dataframes = load_results_dataframes()
    df = pd.concat([df] + results_dataframes, ignore_index=True)

    df = preprocess_dataframe(df)

    match_days = md.match_days

    df = df.dropna()
    df = df.sample(frac=1)
    
    # Add team-based features
    print("Adding team features...")
    df = add_team_features(df)

    max_date = df['Date'].max()
    df['days_since_last_match'] = (max_date - df['Date']).dt.days

    decay_rate = 0.98
    df['sample_weight'] = decay_rate ** df['days_since_last_match']

    # Save a copy with original team names for prediction
    df_original = df.copy()
    
    label_encoders = {
        'HomeTeam': LabelEncoder(),
        'AwayTeam': LabelEncoder()
    }

    df['HomeTeam'] = label_encoders['HomeTeam'].fit_transform(df['HomeTeam'])
    df['AwayTeam'] = label_encoders['AwayTeam'].fit_transform(df['AwayTeam'])

    # Get all feature columns (exclude non-feature columns)
    exclude_cols = ['FTHG', 'FTAG', 'HTHG', 'HTAG', 'FTR', 'HTR', 'HomeTeam_raw', 'AwayTeam_raw', 
                    'Date', 'days_since_last_match', 'sample_weight']
    feature_cols = [col for col in df.columns if col not in exclude_cols and col not in ['HomeTeam', 'AwayTeam']]
    feature_cols = ['HomeTeam', 'AwayTeam'] + [col for col in feature_cols if 'w' in col or 'h2h' in col]
    
    X = df[feature_cols]
    y = df['FTR']
    
    print(f"Number of features: {len(feature_cols)}")
    print(f"Features: {feature_cols}")
    print(f"Target distribution:\n{y.value_counts()}")

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    sample_weights_train = df.loc[X_train.index, 'sample_weight'].values

    # Train RandomForest
    print("\nTraining RandomForest...")
    model = RandomForestClassifier(
        n_estimators=1000, 
        random_state=41,
        max_depth=15,
        min_samples_split=5,
        min_samples_leaf=2,
        class_weight='balanced',
        n_jobs=-1
    )
    model.fit(X_train, y_train, sample_weight=sample_weights_train)
    y_pred = model.predict(X_test)
    acc, report = evaluate_model(y_test, y_pred)
    print(f"Accuracy: {acc:.4f}")
    print(f"Classification Report:\n{report}")

    # Get the next matchday (10) - the first one after completed matchdays in results.py
    next_match_day = 10
    next_match_day_info = match_days[next_match_day]["matches"]

    # Class labels order from the model
    class_labels = model.classes_

    print('Match day number: {}'.format(next_match_day))
    for i in next_match_day_info:
        match = next_match_day_info[i]
        H = match["H"]
        A = match["A"]
        if H and A:
            result, probs = predict_result(H, A, label_encoders, model, df_original, feature_cols)
            result_label = {'H': f'{H} win', 'D': 'Draw', 'A': f'{A} win'}[result]
            # Map probabilities to labels
            prob_dict = dict(zip(class_labels, probs))
            h_prob = prob_dict.get('H', 0)
            d_prob = prob_dict.get('D', 0)
            a_prob = prob_dict.get('A', 0)
            print(f"{i}. {H} vs {A}: {result_label} (H:{h_prob:.1%} D:{d_prob:.1%} A:{a_prob:.1%})")


if __name__ == "__main__":
    main()
