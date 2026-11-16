from dataclasses import dataclass
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

from .features import MatchResult, build_features


@dataclass
class PredictionContext:
    """Groups the prediction-related objects that always travel together."""
    label_encoders: dict
    model: RandomForestClassifier
    df_full: pd.DataFrame
    feature_cols: list


def predict_result(home_team, away_team, context: PredictionContext):
    """Predict match result (H/D/A) with probabilities for a specific match."""
    home_team_encoded = context.label_encoders['HomeTeam'].transform([home_team])
    away_team_encoded = context.label_encoders['AwayTeam'].transform([away_team])

    max_date = context.df_full['Date'].max()

    # Build features using the shared function
    features = build_features(context.df_full, home_team, away_team, max_date)

    # Wrap values in lists for DataFrame creation
    feature_list = {
        'HomeTeam': [home_team_encoded[0]],
        'AwayTeam': [away_team_encoded[0]]
    }
    feature_list.update({k: [v] for k, v in features.items()})

    prediction_input = pd.DataFrame(feature_list)[context.feature_cols]
    prediction = context.model.predict(prediction_input)
    probabilities = context.model.predict_proba(prediction_input)
    return prediction[0], probabilities[0]


def format_prediction(match_index, home_team, away_team, result, probs, class_labels):
    """Format a single prediction result for display."""
    result_label = {
        MatchResult.HOME.value: f'{home_team} win',
        MatchResult.DRAW.value: 'Draw',
        MatchResult.AWAY.value: f'{away_team} win',
    }[result]
    # Map probabilities to labels
    prob_dict = dict(zip(class_labels, probs))
    h_prob = prob_dict.get(MatchResult.HOME.value, 0)
    d_prob = prob_dict.get(MatchResult.DRAW.value, 0)
    a_prob = prob_dict.get(MatchResult.AWAY.value, 0)
    return f"{match_index}. {home_team} vs {away_team}: {result_label} (H:{h_prob:.1%} D:{d_prob:.1%} A:{a_prob:.1%})"
