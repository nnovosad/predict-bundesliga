from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


def evaluate_model(y_true, y_pred):
    """Calculate accuracy and classification report for model evaluation."""
    acc = accuracy_score(y_true, y_pred)
    report = classification_report(y_true, y_pred, target_names=['Home Win (H)', 'Draw (D)', 'Away Win (A)'])
    return acc, report


def prepare_features(df):
    """
    Prepare feature columns and encode team names.
    
    Returns:
        Tuple of (X, y, df_encoded, label_encoders, feature_columns)
    """
    # Save a copy with original team names for prediction
    df_original = df.copy()

    label_encoders = {
        'HomeTeam': LabelEncoder(),
        'AwayTeam': LabelEncoder()
    }

    df_encoded = df.copy()
    df_encoded['HomeTeam'] = label_encoders['HomeTeam'].fit_transform(df_encoded['HomeTeam'])
    df_encoded['AwayTeam'] = label_encoders['AwayTeam'].fit_transform(df_encoded['AwayTeam'])

    # Get all feature columns (exclude non-feature columns)
    exclude_cols = ['FTHG', 'FTAG', 'HTHG', 'HTAG', 'FTR', 'HTR', 'HomeTeam_raw', 'AwayTeam_raw',
                    'Date', 'days_since_last_match', 'sample_weight']
    feature_columns = [col for col in df_encoded.columns if col not in exclude_cols and col not in ['HomeTeam', 'AwayTeam']]
    feature_columns = ['HomeTeam', 'AwayTeam'] + [col for col in feature_columns if 'w' in col or 'h2h' in col]

    X = df_encoded[feature_columns]
    y = df_encoded['FTR']

    return X, y, df_original, label_encoders, feature_columns


def train_random_forest(X_train, y_train, sample_weights):
    """Train a RandomForest classifier with balanced class weights."""
    model = RandomForestClassifier(
        n_estimators=1000,
        random_state=41,
        max_depth=15,
        min_samples_split=5,
        min_samples_leaf=2,
        class_weight='balanced',
        n_jobs=-1
    )
    model.fit(X_train, y_train, sample_weight=sample_weights)
    return model
