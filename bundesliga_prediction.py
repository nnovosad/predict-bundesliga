"""Main entry point for Bundesliga match prediction.

Orchestrates the prediction pipeline by importing modules from the
predict_bundesliga package.
"""
import os
import pandas as pd
from sklearn.model_selection import train_test_split

import match_days
from predict_bundesliga import (
    read_and_concat_files,
    load_results_dataframes,
    preprocess_dataframe,
    add_team_features,
    prepare_features,
    train_random_forest,
    evaluate_model,
    PredictionContext,
    predict_result,
    format_prediction,
)


def main():
    # FTHG: Full Time Home Team Goals
    # HTHG: Half Time Home Team Goals
    # FTAG: Full Time Away Team Goals
    # HTAG: Half Time Away Team Goals
    # FTR: Full Time Result (being either "H", "A" or "D" for "Draw")
    # HTR: Half Time Result (being either "H", "A" or "D" for "Draw")
    # HomeTeam: Name of the home team
    # AwayTeam: Name of the away team

    # Load Kaggle data
    kaggle_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'kaggle', 'input')
    df = read_and_concat_files(kaggle_path)

    print(df[["FTHG", "HTHG", "FTAG", "HTAG", "FTR", "HTR"]].describe())
    print(df[["FTHG", "HTHG", "FTAG", "HTAG", "FTR", "HTR"]].isnull().sum())

    # Load completed results and determine next matchday
    results_dataframes = load_results_dataframes()
    df = pd.concat([df] + results_dataframes, ignore_index=True)

    next_match_day = len(results_dataframes) + 1

    df = preprocess_dataframe(df)
    df = df.dropna()
    df = df.sample(frac=1)

    # Add team-based features
    print("Adding team features...")
    df = add_team_features(df)

    # Add temporal features
    max_date = df['Date'].max()
    df['days_since_last_match'] = (max_date - df['Date']).dt.days
    decay_rate = 0.98
    df['sample_weight'] = decay_rate ** df['days_since_last_match']

    # Prepare features and encode teams
    X, y, df_original, label_encoders, feature_columns = prepare_features(df)

    print(f"Number of features: {len(feature_columns)}")
    print(f"Features: {feature_columns}")
    print(f"Target distribution:\n{y.value_counts()}")

    # Split and train
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    sample_weights_train = df.loc[X_train.index, 'sample_weight'].values

    print("\nTraining RandomForest...")
    model = train_random_forest(X_train, y_train, sample_weights_train)
    y_pred = model.predict(X_test)
    acc, report = evaluate_model(y_test, y_pred)
    print(f"Accuracy: {acc:.4f}")
    print(f"Classification Report:\n{report}")

    # Predict next matchday
    next_match_day_info = match_days.match_days[next_match_day]["matches"]
    class_labels = model.classes_

    prediction_context = PredictionContext(
        label_encoders=label_encoders,
        model=model,
        df_full=df_original,
        feature_cols=feature_columns
    )

    print('Match day number: {}'.format(next_match_day))
    for i in next_match_day_info:
        match = next_match_day_info[i]
        home_team = match["H"]
        away_team = match["A"]
        if home_team and away_team:
            result, probs = predict_result(home_team, away_team, prediction_context)
            print(format_prediction(i, home_team, away_team, result, probs, class_labels))


if __name__ == "__main__":
    main()
