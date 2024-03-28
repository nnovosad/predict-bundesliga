import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error
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
            rs.results_d8, rs.results_d9, rs.results_d10, rs.results_d11, rs.results_d12, rs.results_d13,
            rs.results_d14, rs.results_d15, rs.results_d16, rs.results_d17, rs. results_d18, rs.results_d19,
            rs.results_d20, rs.results_d21, rs.results_d22, rs.results_d23, rs.results_d24, rs.results_d25,
            rs.results_d26]


def preprocess_dataframe(df):
    columns_to_keep = ["FTHG", "HTHG", "FTAG", "HTAG", "FTR", "HTR", "HomeTeam", "AwayTeam", "Date"]
    return df[columns_to_keep]


def train_predict_rf(X_train, y_train, X_test):
    rf = RandomForestRegressor()
    rf.fit(X_train, y_train)
    predictions = rf.predict(X_test)
    return predictions


def evaluate_model(y_true, y_pred):
    r2 = r2_score(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    return r2, mae


def predict_result(home_team, away_team, label_encoders, model):
    home_team_encoded = label_encoders['HomeTeam'].transform([home_team])
    away_team_encoded = label_encoders['AwayTeam'].transform([away_team])
    prediction_input = pd.DataFrame({
        'HomeTeam': [home_team_encoded[0]],
        'AwayTeam': [away_team_encoded[0]]
    })
    prediction = model.predict(prediction_input)
    return prediction[0]


def main():
    df = read_and_concat_files('/Users/nnovosad/PycharmProjects/predict-bundesliga/kaggle')

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

    df.dropna(inplace=True)
    df = df.sample(frac=1)
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

    max_date = df['Date'].max()
    df['days_since_last_match'] = (max_date - df['Date']).dt.days

    decay_rate = 0.98
    df['sample_weight'] = decay_rate ** df['days_since_last_match']

    label_encoders = {
        'HomeTeam': LabelEncoder(),
        'AwayTeam': LabelEncoder()
    }

    df['HomeTeam'] = label_encoders['HomeTeam'].fit_transform(df['HomeTeam'])
    df['AwayTeam'] = label_encoders['AwayTeam'].fit_transform(df['AwayTeam'])

    X = df[['HomeTeam', 'AwayTeam']]
    y = df[['FTHG', "FTAG"]]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    sample_weights_train = df.loc[X_train.index, 'sample_weight'].values

    model = RandomForestRegressor(n_estimators=1000, random_state=41)

    model.fit(X_train, y_train, sample_weight=sample_weights_train)

    y_pred = model.predict(X_test)
    print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
    print("R^2 Score:", r2_score(y_test, y_pred))

    last_match_day = list(match_days.keys())[-1]
    last_match_day_info = match_days[last_match_day]["matches"]

    print('Match day number: {}'.format(last_match_day))
    for i in last_match_day_info:
        match = last_match_day_info[i]
        H = match["H"]
        A = match["A"]
        if H and A:
            r = predict_result(H, A, label_encoders, model)
            print(f"{i}. {H}: {round(r[0])} - {round(r[1])} : {A}")


if __name__ == "__main__":
    main()
