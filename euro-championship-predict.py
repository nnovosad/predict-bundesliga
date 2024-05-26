from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge, Lasso

import pandas as pd
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.preprocessing import LabelEncoder, PolynomialFeatures
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from catboost import CatBoostRegressor

def main():
    matches = pd.read_csv('/Users/nnovosad/PycharmProjects/predict-bundesliga/kaggle/euro-championship/Uefa_Euro_Cup_All_Matches.csv')

    matches['HomeTeamName'] = matches['HomeTeamName'].apply(lambda x: x.replace(u'\xa0', u'')).apply(
        lambda x: x.strip())
    matches['AwayTeamName'] = matches['AwayTeamName'].apply(lambda x: x.replace(u'\xa0', u'')).apply(
        lambda x: x.strip())

    matches.replace('Soviet Union', 'Russia', inplace=True)
    matches.replace('West Germany', 'Germany', inplace=True)

    label_encoders = {
        'HomeTeamName': LabelEncoder(),
        'AwayTeamName': LabelEncoder()
    }

    matches['HomeTeamName'] = label_encoders['HomeTeamName'].fit_transform(matches['HomeTeamName'])
    matches['AwayTeamName'] = label_encoders['AwayTeamName'].fit_transform(matches['AwayTeamName'])

    X = matches[['HomeTeamName', 'AwayTeamName']]
    y = matches[['HomeTeamGoals', 'AwayTeamGoals']]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # model = RandomForestRegressor(random_state=41, max_depth=5, min_samples_leaf=1, min_samples_split=5, n_estimators=1500)
    model = LinearRegression(copy_X=True, fit_intercept=True, positive=True)
    # model = Ridge(alpha=1.0)
    # model = Lasso(alpha=0.1)
    # model = XGBRegressor(n_estimators=100, learning_rate=0.1)

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
    print("R^2 Score:", r2_score(y_test, y_pred))

    home_team = "Italy"
    away_team = "Albania"

    home_team_encoded = label_encoders['HomeTeamName'].transform([home_team])
    away_team_encoded = label_encoders['AwayTeamName'].transform([away_team])
    prediction_input = pd.DataFrame({
        'HomeTeamName': [home_team_encoded[0]],
        'AwayTeamName': [away_team_encoded[0]]
    })
    prediction = model.predict(prediction_input)

    result = prediction[0]

    print(f"{home_team}: {round(result[0])} - {round(result[1])} : {away_team}")

if __name__ == "__main__":
    main()
