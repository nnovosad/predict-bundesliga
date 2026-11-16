"""Predict Bundesliga package for match result prediction."""

from .data_loader import read_and_concat_files, load_results_dataframes, preprocess_dataframe
from .features import (
    MatchResult,
    WindowFeatures,
    H2HFeatures,
    WINDOWS,
    get_team_stats,
    build_window_features,
    build_h2h_features,
    build_features,
    add_team_features,
)
from .model import evaluate_model, prepare_features, train_random_forest
from .predictor import PredictionContext, predict_result, format_prediction

__all__ = [
    # Data loading
    'read_and_concat_files',
    'load_results_dataframes',
    'preprocess_dataframe',
    # Features
    'MatchResult',
    'WindowFeatures',
    'H2HFeatures',
    'WINDOWS',
    'get_team_stats',
    'build_window_features',
    'build_h2h_features',
    'build_features',
    'add_team_features',
    # Model
    'evaluate_model',
    'prepare_features',
    'train_random_forest',
    # Predictor
    'PredictionContext',
    'predict_result',
    'format_prediction',
]
