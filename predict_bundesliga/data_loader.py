import os
import pandas as pd
from tqdm import tqdm

import results


def read_and_concat_files(directory):
    """Read and concatenate all CSV files from a directory tree."""
    file_list = []
    for dirname, _, filenames in os.walk(directory):
        for filename in filenames:
            try:
                pd.read_csv(os.path.join(dirname, filename))
                file_list.append(os.path.join(dirname, filename))
            except Exception as e:
                continue
    return pd.concat((pd.read_csv(f) for f in tqdm(file_list)), ignore_index=True)


def load_results_dataframes():
    """Load completed matchday results from the results module."""
    return [results.results_d1, results.results_d2, results.results_d3, results.results_d4, results.results_d5,
            results.results_d6, results.results_d7, results.results_d8, results.results_d9]


def preprocess_dataframe(df):
    """Keep only the relevant columns for prediction."""
    columns_to_keep = ["FTHG", "HTHG", "FTAG", "HTAG", "FTR", "HTR", "HomeTeam", "AwayTeam", "Date"]
    return df[columns_to_keep]
