"""FastAPI web application for Bundesliga match predictions.

Serves an HTML page with match predictions and expandable details
about model accuracy, classification report, and feature statistics.
"""
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
import jinja2

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

app = FastAPI(title="Bundesliga Predictor")

# Setup Jinja2 directly
_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")),
    autoescape=True,
)
_jinja_env.globals.update(len=len)
template = _jinja_env.get_template("index.html")

# Global prediction cache
prediction_cache = None


def run_prediction_pipeline():
    """Run the full prediction pipeline and return structured results."""
    global prediction_cache
    if prediction_cache is not None:
        return prediction_cache

    # Load Kaggle data
    kaggle_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'kaggle', 'input')
    df = read_and_concat_files(kaggle_path)

    # Collect detailed stats for expandable section
    stats_null = df[["FTHG", "HTHG", "FTAG", "HTAG", "FTR", "HTR"]].isnull().sum()
    stats_null_dict = {str(k): int(v) for k, v in stats_null.items()}

    # Load completed results and determine next matchday
    results_dataframes = load_results_dataframes()
    df = pd.concat([df] + results_dataframes, ignore_index=True)

    next_match_day = len(results_dataframes) + 1

    df = preprocess_dataframe(df)
    df = df.dropna()
    df = df.sample(frac=1)

    # Add team-based features
    df = add_team_features(df)

    # Add temporal features
    max_date = df['Date'].max()
    df['days_since_last_match'] = (max_date - df['Date']).dt.days
    decay_rate = 0.98
    df['sample_weight'] = decay_rate ** df['days_since_last_match']

    # Prepare features and encode teams
    X, y, df_original, label_encoders, feature_columns = prepare_features(df)

    target_distribution = {str(k): int(v) for k, v in y.value_counts().items()}

    # Split and train
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    sample_weights_train = df.loc[X_train.index, 'sample_weight'].values

    model = train_random_forest(X_train, y_train, sample_weights_train)
    y_pred = model.predict(X_test)
    acc, report = evaluate_model(y_test, y_pred)

    # Predict next matchday
    next_match_day_info = match_days.match_days[next_match_day]["matches"]
    class_labels = model.classes_

    prediction_context = PredictionContext(
        label_encoders=label_encoders,
        model=model,
        df_full=df_original,
        feature_cols=feature_columns
    )

    predictions = []
    for i in next_match_day_info:
        match = next_match_day_info[i]
        home_team = match["H"]
        away_team = match["A"]
        if home_team and away_team:
            result, probs = predict_result(home_team, away_team, prediction_context)

            # Parse probabilities
            result_label_map = {
                'H': f'{home_team} win',
                'D': 'Draw',
                'A': f'{away_team} win',
            }
            prob_dict = dict(zip(class_labels, probs))
            h_prob = float(prob_dict.get('H', 0))
            d_prob = float(prob_dict.get('D', 0))
            a_prob = float(prob_dict.get('A', 0))

            predictions.append({
                'match_num': int(i),
                'home_team': home_team,
                'away_team': away_team,
                'result': result_label_map.get(result, 'Draw'),
                'result_code': result,
                'h_prob': round(h_prob * 100, 1),
                'd_prob': round(d_prob * 100, 1),
                'a_prob': round(a_prob * 100, 1),
            })

    result = {
        'match_day': next_match_day,
        'accuracy': round(float(acc), 4),
        'accuracy_pct': round(float(acc) * 100, 2),
        'classification_report': report,
        'predictions': predictions,
        'num_features': len(feature_columns),
        'feature_columns': feature_columns,
        'target_distribution': target_distribution,
        'stats_null': stats_null_dict,
    }
    prediction_cache = result
    return result


@app.get("/favicon.ico")
async def favicon():
    """Return favicon.ico."""
    return FileResponse(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "static", "favicon.ico"),
        media_type="image/x-icon",
    )


@app.get("/", response_class=HTMLResponse)
async def index():
    """Main page with predictions."""
    data = run_prediction_pipeline()
    html = template.render(**data)
    return HTMLResponse(content=html)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
