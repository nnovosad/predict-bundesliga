import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error
from tqdm import tqdm


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
    results_d1 = pd.DataFrame({
        "HomeTeam": ['Werder Bremen', 'Leverkusen', 'Wolfsburg', 'Hoffenheim', 'Augsburg', 'Stuttgart', 'Dortmund',
                     'Union Berlin', 'Ein Frankfurt'],
        "AwayTeam": ['Bayern Munich', 'RB Leipzig', 'Heidenheim', 'Freiburg', "M'gladbach", 'Bochum', 'FC Koln',
                     'Mainz',
                     'Darmstadt'],
        "FTHG": [0, 3, 2, 1, 4, 5, 1, 4, 1],
        "FTAG": [4, 2, 0, 2, 4, 0, 0, 1, 0],
        "HTHG": [0, 2, 2, 0, 3, 2, 0, 2, 1],
        "HTAG": [1, 1, 0, 2, 3, 0, 0, 0, 0],
        "FTR": ['A', 'H', 'H', 'A', 'D', 'H', 'H', 'H', 'H'],
        "HTR": ['A', 'H', 'H', 'A', 'D', 'H', 'D', 'H', 'H'],
        "Date": ['18/08/23', '19/08/23', '19/08/23', '19/08/23', '19/08/23', '19/08/23', '19/08/23', '20/08/23',
                 '20/08/23']
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
        "Date": ['25/08/23', '26/08/23', '26/08/23', '26/08/23', '26/08/23', '26/08/23', '26/08/23', '27/08/23',
                 '27/08/23']
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
        "Date": ['01/09/23', '02/09/23', '02/09/23', '02/09/23', '02/09/23', '02/09/23', '02/09/23', '03/09/23',
                 '03/09/23']
    })
    results_d4 = pd.DataFrame({
        "HomeTeam": ['Bayern Munich', 'RB Leipzig', 'Mainz', 'FC Koln', 'Wolfsburg', 'Freiburg', 'Bochum', 'Heidenheim',
                     'Darmstadt'],
        "AwayTeam": ['Leverkusen', 'Augsburg', 'Stuttgart', 'Hoffenheim', 'Union Berlin', 'Dortmund', 'Ein Frankfurt',
                     'Werder Bremen', "M'gladbach"],
        "FTHG": [2, 3, 1, 1, 2, 2, 1, 4, 3],
        "FTAG": [2, 0, 3, 3, 1, 4, 1, 2, 3],
        "HTHG": [1, 3, 0, 0, 2, 2, 0, 2, 3],
        "HTAG": [1, 0, 0, 2, 1, 1, 0, 0, 0],
        "FTR": ['D', 'H', 'A', 'A', 'H', 'A', 'D', 'H', 'D'],
        "HTR": ['D', 'H', 'D', 'A', 'H', 'H', 'D', 'H', 'H'],
        "Date": ['15/09/23', '16/09/23', '16/09/23', '16/09/23', '16/09/23', '16/09/23', '16/09/23', '17/09/23',
                 '17/09/23']
    })
    results_d5 = pd.DataFrame({
        "HomeTeam": ['Stuttgart', 'Bayern Munich', 'Dortmund', "M'gladbach", 'Augsburg', 'Union Berlin',
                     'Werder Bremen',
                     'Leverkusen', 'Ein Frankfurt'],
        "AwayTeam": ['Darmstadt', 'Bochum', 'Wolfsburg', 'RB Leipzig', 'Mainz', 'Hoffenheim', 'FC Koln', 'Heidenheim',
                     'Freiburg'],
        "FTHG": [3, 7, 1, 0, 2, 0, 2, 4, 0],
        "FTAG": [1, 0, 0, 1, 1, 2, 1, 1, 0],
        "HTHG": [2, 4, 0, 0, 2, 0, 1, 1, 0],
        "HTAG": [1, 0, 0, 0, 1, 2, 1, 0, 0],
        "FTR": ['H', 'H', 'H', 'A', 'H', 'A', 'H', 'H', 'D'],
        "HTR": ['H', 'H', 'D', 'D', 'H', 'A', 'D', 'H', 'D'],
        "Date": ['22/09/23', '23/09/23', '23/09/23', '23/09/23', '23/09/23', '23/09/23', '23/09/23', '24/09/23',
                 '24/09/23']
    })
    results_d6 = pd.DataFrame({
        "HomeTeam": ['Hoffenheim', 'Mainz', 'Heidenheim', 'FC Koln', 'Wolfsburg', 'Bochum', 'RB Leipzig', 'Darmstadt',
                     'Freiburg'],
        "AwayTeam": ['Dortmund', 'Leverkusen', 'Union Berlin', 'Stuttgart', 'Ein Frankfurt', "M'gladbach",
                     'Bayern Munich',
                     'Werder Bremen', 'Augsburg'],
        "FTHG": [1, 0, 1, 0, 2, 1, 2, 4, 2],
        "FTAG": [3, 3, 0, 2, 0, 3, 2, 2, 0],
        "HTHG": [1, 0, 0, 0, 1, 0, 2, 2, 1],
        "HTAG": [2, 1, 0, 0, 0, 3, 0, 0, 0],
        "FTR": ['A', 'A', 'H', 'A', 'H', 'A', 'H', 'H', 'H'],
        "HTR": ['A', 'A', 'D', 'D', 'H', 'A', 'D', 'H', 'H'],
        "Date": ['29/09/23', '30/09/23', '30/09/23', '30/09/23', '30/09/23', '30/09/23', '30/09/23', '01/10/23',
                 '01/10/23']
    })
    results_d7 = pd.DataFrame({
        "HomeTeam": ["M'gladbach", 'RB Leipzig', 'Augsburg', 'Dortmund', 'Stuttgart', 'Werder Bremen', 'Leverkusen',
                     'Bayern Munich', 'Ein Frankfurt'],
        "AwayTeam": ['Mainz', 'Bochum', 'Darmstadt', 'Union Berlin', 'Wolfsburg', 'Hoffenheim', 'FC Koln', 'Freiburg',
                     'Heidenheim'],
        "FTHG": [2, 0, 1, 4, 3, 2, 3, 3, 2],
        "FTAG": [2, 0, 2, 2, 1, 3, 0, 0, 0],
        "HTHG": [1, 0, 0, 1, 0, 1, 2, 2, 1],
        "HTAG": [1, 0, 0, 2, 1, 2, 0, 0, 0],
        "FTR": ['D', 'D', 'D', 'H', 'H', 'A', 'H', 'H', 'H'],
        "HTR": ['D', 'D', 'A', 'A', 'A', 'A', 'H', 'H', 'H'],
        "Date": ['06/10/23', '07/10/23', '07/10/23', '07/10/23', '07/10/23', '07/10/23', '08/10/23', '08/10/23',
                 '08/10/23']
    })
    results_d8 = pd.DataFrame({
        "HomeTeam": ['Dortmund', 'Wolfsburg', 'Union Berlin', 'Hoffenheim', 'Darmstadt', 'Freiburg', 'Mainz', 'FC Koln',
                     'Heidenheim'],
        "AwayTeam": ['Werder Bremen', 'Leverkusen', 'Stuttgart', 'Ein Frankfurt', 'RB Leipzig', 'Bochum',
                     'Bayern Munich',
                     "M'gladbach", 'Augsburg'],
        "FTHG": [1, 1, 0, 1, 1, 2, 1, 3, 2],
        "FTAG": [0, 2, 3, 3, 3, 1, 3, 1, 5],
        "HTHG": [0, 1, 0, 1, 1, 2, 1, 1, 2],
        "HTAG": [0, 1, 1, 3, 2, 1, 2, 0, 3],
        "FTR": ['H', 'A', 'A', 'A', 'A', 'H', 'A', 'H', 'A'],
        "HTR": ['D', 'D', 'A', 'A', 'A', 'H', 'A', 'H', 'A'],
        "Date": ['20/10/23', '21/10/23', '21/10/23', '21/10/23', '21/10/23', '21/10/23', '21/10/23', '22/10/23',
                 '22/10/23']
    })
    results_d9 = pd.DataFrame({
        "HomeTeam": ['Bochum', "M'gladbach", 'Bayern Munich', 'Augsburg', 'Stuttgart', 'Werder Bremen', 'RB Leipzig',
                     'Ein Frankfurt', 'Leverkusen'],
        "AwayTeam": ['Mainz', 'Heidenheim', 'Darmstadt', 'Wolfsburg', 'Hoffenheim', 'Union Berlin', 'FC Koln',
                     'Dortmund',
                     'Freiburg'],
        "FTHG": [2, 2, 8, 3, 2, 2, 6, 3, 2],
        "FTAG": [2, 1, 0, 2, 3, 0, 0, 3, 1],
        "HTHG": [1, 1, 0, 1, 0, 1, 4, 2, 1],
        "HTAG": [0, 1, 0, 2, 2, 0, 0, 1, 0],
        "FTR": ['D', 'H', 'H', 'H', 'A', 'H', 'H', 'D', 'H'],
        "HTR": ['H', 'D', 'D', 'A', 'A', 'H', 'H', 'H', 'H'],
        "Date": ['27/10/23', '28/10/23', '28/10/23', '28/10/23', '28/10/23', '28/10/23', '28/10/23', '29/10/23',
                 '29/10/23']
    })
    results_d10 = pd.DataFrame({
        "HomeTeam": ['Darmstadt', 'Hoffenheim', 'Mainz', 'Freiburg', 'Union Berlin', 'FC Koln', 'Dortmund', 'Wolfsburg',
                     'Heidenheim'],
        "AwayTeam": ['Bochum', 'Leverkusen', 'RB Leipzig', "M'gladbach", 'Ein Frankfurt', 'Augsburg', 'Bayern Munich',
                     'Werder Bremen', 'Stuttgart'],
        "FTHG": [1, 2, 2, 3, 0, 1, 0, 2, 2],
        "FTAG": [2, 3, 0, 3, 3, 1, 4, 2, 0],
        "HTHG": [1, 0, 0, 1, 0, 1, 0, 1, 0],
        "HTAG": [1, 2, 0, 3, 2, 1, 2, 1, 0],
        "FTR": ['A', 'A', 'H', 'D', 'A', 'D', 'A', 'D', 'H'],
        "HTR": ['D', 'A', 'D', 'A', 'A', 'D', 'A', 'D', 'D'],
        "Date": ['03/11/23', '04/11/23', '04/11/23', '04/11/23', '04/11/23', '04/11/23', '04/11/23', '05/11/23',
                 '05/11/23']
    })
    results_d11 = pd.DataFrame({
        "HomeTeam": ["M'gladbach", 'Augsburg', 'Stuttgart', 'Bayern Munich', 'Darmstadt', 'Bochum', 'Leverkusen',
                     'Werder Bremen', 'RB Leipzig'],
        "AwayTeam": ['Wolfsburg', 'Hoffenheim', 'Dortmund', 'Heidenheim', 'Mainz', 'FC Koln', 'Union Berlin',
                     'Ein Frankfurt', 'Freiburg'],
        "FTHG": [4, 1, 2, 4, 0, 1, 4, 2, 3],
        "FTAG": [0, 1, 1, 2, 0, 1, 0, 2, 1],
        "HTHG": [2, 0, 1, 2, 0, 1, 1, 1, 1],
        "HTAG": [0, 1, 1, 0, 0, 0, 0, 0, 1],
        "FTR": ['H', 'D', 'H', 'H', 'D', 'D', 'H', 'D', 'H'],
        "HTR": ['H', 'A', 'D', 'H', 'D', 'H', 'H', 'H', 'D'],
        "Date": ['10/11/23', '11/11/23', '11/11/23', '11/11/23', '11/11/23', '11/11/23', '12/11/23', '12/11/23',
                 '12/11/23']
    })
    results_d12 = pd.DataFrame({
        "HomeTeam": ['FC Koln', 'Werder Bremen', 'Freiburg', 'Wolfsburg', 'Dortmund', 'Union Berlin', 'Ein Frankfurt',
                     'Heidenheim', 'Hoffenheim'],
        "AwayTeam": ['Bayern Munich', 'Leverkusen', 'Darmstadt', 'RB Leipzig', "M'gladbach", 'Augsburg', 'Stuttgart',
                     'Bochum', 'Mainz'],
        "FTHG": [0, 0, 1, 2, 4, 1, 1, 0, 1],
        "FTAG": [1, 3, 1, 1, 2, 1, 2, 0, 1],
        "HTHG": [0, 0, 1, 1, 3, 0, 1, 0, 0],
        "HTAG": [1, 2, 1, 0, 2, 1, 2, 0, 1],
        "FTR": ['A', 'A', 'D', 'H', 'H', 'D', 'A', 'D', 'A'],
        "HTR": ['A', 'A', 'D', 'H', 'H', 'A', 'A', 'D', 'D'],
        "Date": ['24/11/23', '25/11/23', '25/11/23', '25/11/23', '25/11/23', '25/11/23', '25/11/23', '26/11/23',
                 '26/11/23']
    })
    results_d13 = pd.DataFrame({
        "HomeTeam": ['Darmstadt', 'RB Leipzig', "M'gladbach", 'Bochum', 'Stuttgart', 'Mainz', 'Leverkusen', 'Augsburg'],
        "AwayTeam": ['FC Koln', 'Heidenheim', 'Hoffenheim', 'Wolfsburg', 'Werder Bremen', 'Freiburg', 'Dortmund', 'Ein Frankfurt'],
        "FTHG": [0, 2, 2, 3, 2, 0, 1, 2],
        "FTAG": [1, 1, 1, 1, 0, 1, 1, 1],
        "HTHG": [0, 2, 0, 2, 1, 0, 0, 1],
        "HTAG": [0, 1, 0, 1, 0, 0, 1, 0],
        "FTR": ['A', 'H', 'H', 'H', 'H', 'A', 'D', 'H'],
        "HTR": ['D', 'H', 'D', 'H', 'H', 'D', 'A', 'H'],
        "Date": ['01/12/23', '02/12/23', '02/12/23', '02/12/23', '02/12/23', '03/12/23', '03/12/23', '03/12/23']
    })
    results_d14 = pd.DataFrame({
        "HomeTeam": ['Hoffenheim', 'Wolfsburg', 'Heidenheim', 'Union Berlin', 'Werder Bremen', 'Ein Frankfurt', 'Dortmund', 'Stuttgart', 'FC Koln'],
        "AwayTeam": ['Bochum', 'Freiburg', 'Darmstadt', "M'gladbach", 'Augsburg', 'Bayern Munich', 'RB Leipzig', 'Leverkusen', 'Mainz'],
        "FTHG": [3, 0, 3, 3, 2, 5, 2, 1, 0],
        "FTAG": [1, 1, 2, 1, 0, 1, 3, 1, 0],
        "HTHG": [2, 0, 1, 1, 1, 3, 1, 1, 0],
        "HTAG": [0, 0, 0, 0, 0, 1, 1, 0, 0],
        "FTR": ['H', 'A', 'H', 'H', 'H', 'H', 'A', 'D', 'D'],
        "HTR": ['H', 'D', 'H', 'H', 'H', 'H', 'D', 'H', 'D'],
        "Date": ['08/12/23', '09/12/23', '09/12/23', '09/12/23', '09/12/23', '09/12/23', '09/12/23', '10/12/23', '10/12/23']
    })
    results_empty = pd.DataFrame({
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

    return [results_d1, results_d2, results_d3, results_d4, results_d5, results_d6, results_d7, results_d8,
            results_d9, results_d10, results_d11, results_d12, results_d13, results_d14]


def preprocess_dataframe(df):
    columns_to_keep = ["FTHG", "HTHG", "FTAG", "HTAG", "FTR", "HTR", "HomeTeam", "AwayTeam", "Date"]
    return df[columns_to_keep]


def create_match_days():
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
        5: {
            "matches": {
                1: {
                    "H": "Stuttgart",
                    "A": "Darmstadt"
                },
                2: {
                    "H": "Bayern Munich",
                    "A": "Bochum"
                },
                3: {
                    "H": "Dortmund",
                    "A": "Wolfsburg"
                },
                4: {
                    "H": "M'gladbach",
                    "A": "RB Leipzig"
                },
                5: {
                    "H": "Augsburg",
                    "A": "Mainz",
                },
                6: {
                    "H": "Union Berlin",
                    "A": "Hoffenheim"
                },
                7: {
                    "H": "Werder Bremen",
                    "A": "FC Koln"
                },
                8: {
                    "H": "Leverkusen",
                    "A": "Heidenheim"
                },
                9: {
                    "H": "Ein Frankfurt",
                    "A": "Freiburg"
                }
            }
        },
        6: {
            "matches": {
                1: {
                    "H": "Hoffenheim",
                    "A": "Dortmund"
                },
                2: {
                    "H": "Mainz",
                    "A": "Leverkusen"
                },
                3: {
                    "H": "Heidenheim",
                    "A": "Union Berlin"
                },
                4: {
                    "H": "FC Koln",
                    "A": "Stuttgart"
                },
                5: {
                    "H": "Wolfsburg",
                    "A": "Ein Frankfurt",
                },
                6: {
                    "H": "Bochum",
                    "A": "M'gladbach"
                },
                7: {
                    "H": "RB Leipzig",
                    "A": "Bayern Munich"
                },
                8: {
                    "H": "Darmstadt",
                    "A": "Werder Bremen"
                },
                9: {
                    "H": "Freiburg",
                    "A": "Augsburg"
                }
            }
        },
        7: {
            "matches": {
                1: {
                    "H": "M'gladbach",
                    "A": "Mainz"
                },
                2: {
                    "H": "RB Leipzig",
                    "A": "Bochum"
                },
                3: {
                    "H": "Augsburg",
                    "A": "Darmstadt"
                },
                4: {
                    "H": "Dortmund",
                    "A": "Union Berlin"
                },
                5: {
                    "H": "Stuttgart",
                    "A": "Wolfsburg",
                },
                6: {
                    "H": "Werder Bremen",
                    "A": "Hoffenheim"
                },
                7: {
                    "H": "Leverkusen",
                    "A": "FC Koln"
                },
                8: {
                    "H": "Bayern Munich",
                    "A": "Freiburg"
                },
                9: {
                    "H": "Ein Frankfurt",
                    "A": "Heidenheim"
                }
            }
        },
        8: {
            "matches": {
                1: {
                    "H": "Dortmund",
                    "A": "Werder Bremen"
                },
                2: {
                    "H": "Wolfsburg",
                    "A": "Leverkusen"
                },
                3: {
                    "H": "Union Berlin",
                    "A": "Stuttgart"
                },
                4: {
                    "H": "Hoffenheim",
                    "A": "Ein Frankfurt"
                },
                5: {
                    "H": "Darmstadt",
                    "A": "RB Leipzig",
                },
                6: {
                    "H": "Darmstadt",
                    "A": "Bochum"
                },
                7: {
                    "H": "Mainz",
                    "A": "Bayern Munich"
                },
                8: {
                    "H": "FC Koln",
                    "A": "M'gladbach"
                },
                9: {
                    "H": "Heidenheim",
                    "A": "Augsburg"
                }
            }
        },
        9: {
            "matches": {
                1: {
                    "H": "Bochum",
                    "A": "Mainz"
                },
                2: {
                    "H": "M'gladbach",
                    "A": "Heidenheim"
                },
                3: {
                    "H": "Bayern Munich",
                    "A": "Darmstadt"
                },
                4: {
                    "H": "Augsburg",
                    "A": "Wolfsburg"
                },
                5: {
                    "H": "Stuttgart",
                    "A": "Hoffenheim",
                },
                6: {
                    "H": "Werder Bremen",
                    "A": "Union Berlin"
                },
                7: {
                    "H": "RB Leipzig",
                    "A": "FC Koln"
                },
                8: {
                    "H": "Ein Frankfurt",
                    "A": "Dortmund"
                },
                9: {
                    "H": "Leverkusen",
                    "A": "Freiburg"
                }
            }
        },
        10: {
            "matches": {
                1: {
                    "H": "Darmstadt",
                    "A": "Bochum"
                },
                2: {
                    "H": "Hoffenheim",
                    "A": "Leverkusen"
                },
                3: {
                    "H": "Mainz",
                    "A": "RB Leipzig"
                },
                4: {
                    "H": "Freiburg",
                    "A": "M'gladbach"
                },
                5: {
                    "H": "Union Berlin",
                    "A": "Ein Frankfurt",
                },
                6: {
                    "H": "FC Koln",
                    "A": "Augsburg"
                },
                7: {
                    "H": "Dortmund",
                    "A": "Bayern Munich"
                },
                8: {
                    "H": "Wolfsburg",
                    "A": "Werder Bremen"
                },
                9: {
                    "H": "Heidenheim",
                    "A": "Stuttgart"
                }
            }
        },
        11: {
            "matches": {
                1: {
                    "H": "M'gladbach",
                    "A": "Wolfsburg"
                },
                2: {
                    "H": "Augsburg",
                    "A": "Hoffenheim"
                },
                3: {
                    "H": "Stuttgart",
                    "A": "Dortmund"
                },
                4: {
                    "H": "Bayern Munich",
                    "A": "Heidenheim"
                },
                5: {
                    "H": "Darmstadt",
                    "A": "Mainz",
                },
                6: {
                    "H": "Bochum",
                    "A": "FC Koln"
                },
                7: {
                    "H": "Leverkusen",
                    "A": "Union Berlin"
                },
                8: {
                    "H": "Werder Bremen",
                    "A": "Ein Frankfurt"
                },
                9: {
                    "H": "RB Leipzig",
                    "A": "Freiburg"
                }
            }
        },
        12: {
            "matches": {
                1: {
                    "H": "FC Koln",
                    "A": "Bayern Munich"
                },
                2: {
                    "H": "Dortmund",
                    "A": "M'gladbach"
                },
                3: {
                    "H": "Union Berlin",
                    "A": "Augsburg"
                },
                4: {
                    "H": "Freiburg",
                    "A": "Darmstadt"
                },
                5: {
                    "H": "Wolfsburg",
                    "A": "RB Leipzig",
                },
                6: {
                    "H": "Werder Bremen",
                    "A": "Leverkusen"
                },
                7: {
                    "H": "Ein Frankfurt",
                    "A": "Stuttgart"
                },
                8: {
                    "H": "Heidenheim",
                    "A": "Bochum"
                },
                9: {
                    "H": "Hoffenheim",
                    "A": "Mainz"
                }
            }
        },
        13: {
            "matches": {
                1: {
                    "H": "Darmstadt",
                    "A": "FC Koln"
                },
                2: {
                    "H": "RB Leipzig",
                    "A": "Heidenheim"
                },
                3: {
                    "H": "M'gladbach",
                    "A": "Hoffenheim"
                },
                4: {
                    "H": "Bochum",
                    "A": "Wolfsburg",
                },
                5: {
                    "H": "Stuttgart",
                    "A": "Werder Bremen"
                },
                6: {
                    "H": "Mainz",
                    "A": "Freiburg"
                },
                7: {
                    "H": "Leverkusen",
                    "A": "Dortmund"
                },
                8: {
                    "H": "Augsburg",
                    "A": "Ein Frankfurt"
                }
            }
        },
        14: {
            "matches": {
                1: {
                    "H": "Hoffenheim",
                    "A": "Bochum"
                },
                2: {
                    "H": "Union Berlin",
                    "A": "M'gladbach"
                },
                3: {
                    "H": "Ein Frankfurt",
                    "A": "Bayern Munich"
                },
                4: {
                    "H": "Wolfsburg",
                    "A": "Freiburg"
                },
                5: {
                    "H": "Werder Bremen",
                    "A": "Augsburg",
                },
                6: {
                    "H": "Heidenheim",
                    "A": "Darmstadt"
                },
                7: {
                    "H": "Dortmund",
                    "A": "RB Leipzig"
                },
                8: {
                    "H": "Stuttgart",
                    "A": "Leverkusen"
                },
                9: {
                    "H": "FC Koln",
                    "A": "Mainz"
                }
            }
        },
        15: {
            "matches": {
                1: {
                    "H": "M'gladbach",
                    "A": "Werder Bremen"
                },
                2: {
                    "H": "Mainz",
                    "A": "Heidenheim"
                },
                3: {
                    "H": "Bochum",
                    "A": "Union Berlin"
                },
                4: {
                    "H": "Augsburg",
                    "A": "Dortmund"
                },
                5: {
                    "H": "Darmstadt",
                    "A": "Wolfsburg",
                },
                6: {
                    "H": "RB Leipzig",
                    "A": "Hoffenheim"
                },
                7: {
                    "H": "Freiburg",
                    "A": "FC Koln"
                },
                8: {
                    "H": "Leverkusen",
                    "A": "Ein Frankfurt"
                },
                9: {
                    "H": "Bayern Munich",
                    "A": "Stuttgart"
                }
            }
        },
    }

    return match_days


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

    match_days = create_match_days()

    df.dropna(inplace=True)
    df = df.sample(frac=1)
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

    print(np.sort(df["AwayTeam"].unique()))
    print(np.sort(df["HomeTeam"].unique()))

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

    for n in match_days:
        match_day = match_days[n]["matches"]
        print('Match day number: {}'.format(n))
        for i in match_day:
            match = match_day[i]
            H = match["H"]
            A = match["A"]
            if H and A:
                r = predict_result(H, A, label_encoders, model)
                print(f"{H}: {round(r[0])} - {round(r[1])} : {A}")


if __name__ == "__main__":
    main()
