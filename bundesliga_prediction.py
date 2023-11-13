# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All"
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, explained_variance_score
from tqdm import tqdm

fnames = []
for dirname, _, filenames in os.walk('/Users/nnovosad/PycharmProjects/pythonProject/football/kaggle/input'):
    for filename in filenames:
        try:
            pd.read_csv(os.path.join(dirname, filename))
            fnames.append(os.path.join(dirname, filename))
        except Exception as e:
            continue
# print(len(filenames))

df = pd.concat((pd.read_csv(f) for f in tqdm(fnames)), ignore_index=True)

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

df = df[["FTHG", "HTHG", "FTAG", "HTAG", "FTR", "HTR", "HomeTeam", "AwayTeam", "Date"]]

results_d1 = pd.DataFrame({
    "HomeTeam": ['Werder Bremen', 'Leverkusen', 'Wolfsburg', 'Hoffenheim', 'Augsburg', 'Stuttgart', 'Dortmund',
                 'Union Berlin', 'Ein Frankfurt'],
    "AwayTeam": ['Bayern Munich', 'RB Leipzig', 'Heidenheim', 'Freiburg', "M'gladbach", 'Bochum', 'FC Koln', 'Mainz',
                 'Darmstadt'],
    "FTHG": [0, 3, 2, 1, 4, 5, 1, 4, 1],
    "FTAG": [4, 2, 0, 2, 4, 0, 0, 1, 0],
    "HTHG": [0, 2, 2, 0, 3, 2, 0, 2, 1],
    "HTAG": [1, 1, 0, 2, 3, 0, 0, 0, 0],
    "FTR": ['A', 'H', 'H', 'A', 'D', 'H', 'H', 'H', 'H'],
    "HTR": ['A', 'H', 'H', 'A', 'D', 'H', 'D', 'H', 'H'],
    "Date": ['18/08/23', '19/08/23', '19/08/23', '19/08/23', '19/08/23', '19/08/23', '19/08/23', '20/08/23', '20/08/23']
})
results_d2 = pd.DataFrame({
    "HomeTeam": ['RB Leipzig', 'Freiburg', 'FC Koln', 'Bochum', 'Heidenheim', 'Darmstadt', "M'gladbach", 'Mainz',
                 'Bayern Munich'],
    "AwayTeam": ['Stuttgart', 'Werder Bremen', 'Wolfsburg', 'Dortmund', 'Hoffenheim', 'Union Berlin', 'Leverkusen',
                 'Ein Frankfurt', 'Augsburg'],
    "FTHG": [5, 1, 1, 1, 2, 1, 0, 1, 3],
    "FTAG": [1, 0, 2, 1, 3, 4, 3, 1, 1],
    "HTHG": [0, 0, 0, 1, 1, 1, 0, 1, 2],
    "HTAG": [1, 0, 0, 0, 0, 3, 2, 0, 0],
    "FTR": ['H', 'H', 'A', 'D', 'A', 'A', 'A', 'D', 'H'],
    "HTR": ['A', 'D', 'D', 'H', 'H', 'A', 'A', 'H', 'H'],
    "Date": ['25/08/23', '26/08/23', '26/08/23', '26/08/23', '26/08/23', '26/08/23', '26/08/23', '27/08/23', '27/08/23']
})
results_d3 = pd.DataFrame({
    "HomeTeam": ['Dortmund', 'Leverkusen', 'Hoffenheim', 'Werder Bremen', 'Augsburg', 'Stuttgart', "M'gladbach",
                 'Ein Frankfurt', 'Union Berlin'],
    "AwayTeam": ['Heidenheim', 'Darmstadt', 'Wolfsburg', 'Mainz', 'Bochum', 'Freiburg', 'Bayern Munich', 'FC Koln',
                 'RB Leipzig'],
    "FTHG": [2, 5, 3, 4, 2, 5, 1, 1, 0],
    "FTAG": [2, 1, 1, 0, 2, 0, 2, 1, 3],
    "HTHG": [2, 1, 1, 1, 1, 3, 1, 0, 0],
    "HTAG": [0, 1, 1, 0, 1, 0, 0, 1, 0],
    "FTR": ['D', 'H', 'H', 'H', 'D', 'H', 'A', 'D', 'A'],
    "HTR": ['H', 'D', 'D', 'H', 'D', 'H', 'H', 'A', 'D'],
    "Date": ['01/09/23', '02/09/23', '02/09/23', '02/09/23', '02/09/23', '02/09/23', '02/09/23', '03/09/23', '03/09/23']
})
results_d4 = pd.DataFrame({
    "HomeTeam": ['Bayern Munich', 'RB Leipzig', 'Mainz', 'FC Koln', 'Wolfsburg', 'Freiburg', 'Bochum', 'Heidenheim', 'Darmstadt'],
    "AwayTeam": ['Leverkusen', 'Augsburg', 'Stuttgart', 'Hoffenheim', 'Union Berlin', 'Dortmund', 'Ein Frankfurt', 'Werder Bremen', "M'gladbach"],
    "FTHG": [2, 3, 1, 1, 2, 2, 1, 4, 3],
    "FTAG": [2, 0, 3, 3, 1, 4, 1, 2, 3],
    "HTHG": [1, 3, 0, 0, 2, 2, 0, 2, 3],
    "HTAG": [1, 0, 0, 2, 1, 1, 0, 0, 0],
    "FTR": ['D', 'H', 'A', 'A', 'H', 'A', 'D', 'H', 'D'],
    "HTR": ['D', 'H', 'D', 'A', 'H', 'H', 'D', 'H', 'H'],
    "Date": ['15/09/23', '16/09/23', '16/09/23', '16/09/23', '16/09/23', '16/09/23', '16/09/23', '17/09/23', '17/09/23']
})
results_d5 = pd.DataFrame({
    "HomeTeam": ['Stuttgart', 'Bayern Munich', 'Dortmund', "M'gladbach", 'Augsburg', 'Union Berlin', 'Werder Bremen', 'Leverkusen', 'Ein Frankfurt'],
    "AwayTeam": ['Darmstadt', 'Bochum', 'Wolfsburg', 'RB Leipzig', 'Mainz', 'Hoffenheim', 'FC Koln', 'Heidenheim', 'Freiburg'],
    "FTHG": [3, 7, 1, 0, 2, 0, 2, 4, 0],
    "FTAG": [1, 0, 0, 1, 1, 2, 1, 1, 0],
    "HTHG": [2, 4, 0, 0, 2, 0, 1, 1, 0],
    "HTAG": [1, 0, 0, 0, 1, 2, 1, 0, 0],
    "FTR": ['H', 'H', 'H', 'A', 'H', 'A', 'H', 'H', 'D'],
    "HTR": ['H', 'H', 'D', 'D', 'H', 'A', 'D', 'H', 'D'],
    "Date": ['22/09/23', '23/09/23', '23/09/23', '23/09/23', '23/09/23', '23/09/23', '23/09/23', '24/09/23', '24/09/23']
})
results_d6 = pd.DataFrame({
    "HomeTeam": ['Hoffenheim', 'Mainz', 'Heidenheim', 'FC Koln', 'Wolfsburg', 'Bochum', 'RB Leipzig', 'Darmstadt', 'Freiburg'],
    "AwayTeam": ['Dortmund', 'Leverkusen', 'Union Berlin', 'Stuttgart', 'Ein Frankfurt', "M'gladbach", 'Bayern Munich', 'Werder Bremen', 'Augsburg'],
    "FTHG": [1, 0, 1, 0, 2, 1, 2, 4, 2],
    "FTAG": [3, 3, 0, 2, 0, 3, 2, 2, 0],
    "HTHG": [1, 0, 0, 0, 1, 0, 2, 2, 1],
    "HTAG": [2, 1, 0, 0, 0, 3, 0, 0, 0],
    "FTR": ['A', 'A', 'H', 'A', 'H', 'A', 'H', 'H', 'H'],
    "HTR": ['A', 'A', 'D', 'D', 'H', 'A', 'D', 'H', 'H'],
    "Date": ['29/09/23', '30/09/23', '30/09/23', '30/09/23', '30/09/23', '30/09/23', '30/09/23', '01/10/23', '01/10/23']
})
results_d7 = pd.DataFrame({
    "HomeTeam": [],
    "AwayTeam": [],
    "FTHG": [],
    "FTAG": [],
    "HTHG": [],
    "HTAG": [],
    "FTR": [],
    "HTR": [],
    "Date": []
})
results_d8 = pd.DataFrame({
    "HomeTeam": [],
    "AwayTeam": [],
    "FTHG": [],
    "FTAG": [],
    "HTHG": [],
    "HTAG": [],
    "FTR": [],
    "HTR": [],
    "Date": []
})
results_d9 = pd.DataFrame({
    "HomeTeam": [],
    "AwayTeam": [],
    "FTHG": [],
    "FTAG": [],
    "HTHG": [],
    "HTAG": [],
    "FTR": [],
    "HTR": [],
    "Date": []
})
results_d10 = pd.DataFrame({
    "HomeTeam": [],
    "AwayTeam": [],
    "FTHG": [],
    "FTAG": [],
    "HTHG": [],
    "HTAG": [],
    "FTR": [],
    "HTR": [],
    "Date": []
})
results_d11 = pd.DataFrame({
    "HomeTeam": [],
    "AwayTeam": [],
    "FTHG": [],
    "FTAG": [],
    "HTHG": [],
    "HTAG": [],
    "FTR": [],
    "HTR": [],
    "Date": []
})

df = pd.concat([df, results_d1, results_d2, results_d3], ignore_index=True)

match_days = {
    1: {
        "matches": {
            1: {
                "H": "Werder Bremen",
                "A": "Bayern Munich"
            },
            2: {
                "H": "Leverkusen",
                "A": "RB Leipzig"
            },
            3: {
                "H": "Augsburg",
                "A": "M'gladbach"
            },
            4: {
                "H": "Hoffenheim",
                "A": "Freiburg"
            },
            5: {
                "H": "Stuttgart",
                "A": "Bochum",
            },
            6: {
                "H": "Wolfsburg",
                "A": None
            },
            7: {
                "H": "Dortmund",
                "A": "FC Koln"
            },
            8: {
                "H": "Union Berlin",
                "A": "Mainz"
            },
            9: {
                "H": "Ein Frankfurt",
                "A": "Darmstadt"
            }
        }
    },
    2: {
        "matches": {
            1: {
                "H": "RB Leipzig",
                "A": "Stuttgart"
            },
            2: {
                "H": None,
                "A": "Hoffenheim"
            },
            3: {
                "H": "FC Koln",
                "A": "Wolfsburg"
            },
            4: {
                "H": "Freiburg",
                "A": "Werder Bremen"
            },
            5: {
                "H": "Darmstadt",
                "A": "Union Berlin",
            },
            6: {
                "H": "Bochum",
                "A": "Dortmund"
            },
            7: {
                "H": "M'gladbach",
                "A": "Leverkusen"
            },
            8: {
                "H": "Mainz",
                "A": "Ein Frankfurt"
            },
            9: {
                "H": "Bayern Munich",
                "A": "Augsburg"
            }
        }
    },
    3: {
        "matches": {
            1: {
                "H": "Dortmund",
                "A": "Heidenheim"
            },
            2: {
                "H": "Leverkusen",
                "A": "Darmstadt"
            },
            3: {
                "H": "Hoffenheim",
                "A": "Wolfsburg"
            },
            4: {
                "H": "Werder Bremen",
                "A": "Mainz"
            },
            5: {
                "H": "Augsburg",
                "A": "Bochum",
            },
            6: {
                "H": "Stuttgart",
                "A": "Freiburg"
            },
            7: {
                "H": "M'gladbach",
                "A": "Bayern Munich"
            },
            8: {
                "H": "Ein Frankfurt",
                "A": "FC Koln"
            },
            9: {
                "H": "Union Berlin",
                "A": "RB Leipzig"
            }
        }
    },
    4: {
        "matches": {
            1: {
                "H": "Bayern Munich",
                "A": "Leverkusen"
            },
            2: {
                "H": "RB Leipzig",
                "A": "Augsburg"
            },
            3: {
                "H": "Freiburg",
                "A": "Dortmund"
            },
            4: {
                "H": "Wolfsburg",
                "A": "Union Berlin"
            },
            5: {
                "H": "Mainz",
                "A": "Stuttgart",
            },
            6: {
                "H": "FC Koln",
                "A": "Hoffenheim"
            },
            7: {
                "H": "Bochum",
                "A": "Ein Frankfurt"
            },
            8: {
                "H": "Heidenheim",
                "A": "Werder Bremen"
            },
            9: {
                "H": "Darmstadt",
                "A": "M'gladbach"
            }
        }
    },
}

df.dropna(inplace=True)
df = df.sample(frac=1)  # random shuffing.
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

print(np.sort(df["AwayTeam"].unique()))
print(np.sort(df["HomeTeam"].unique()))

max_date = df['Date'].max()
df['days_since_last_match'] = (max_date - df['Date']).dt.days

# Using exponential decay to weight recent matches higher
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


def predict_result(home_team, away_team):
    home_team_encoded = label_encoders['HomeTeam'].transform([home_team])
    away_team_encoded = label_encoders['AwayTeam'].transform([away_team])
    prediction_input = pd.DataFrame({
        'HomeTeam': [home_team_encoded[0]],
        'AwayTeam': [away_team_encoded[0]]
    })
    prediction = model.predict(prediction_input)
    return prediction[0]


for n in match_days:
    match_day = match_days[n]["matches"]
    print('Match day number: {}'.format(n))
    for i in match_day:
        match = match_day[i]
        H = match["H"]
        A = match["A"]
        if H and A:
            r = predict_result(H, A)
            print(f"{H}: {round(r[0])} - {round(r[1])} : {A}")