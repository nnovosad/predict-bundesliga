import pandas as pd

results_d1 = pd.DataFrame({
    "HomeTeam": ['Bayern Munich', 'Elversberg', 'FC Koln', 'Mainz', 'RB Leipzig', 'Union Berlin', 'Dortmund', 'Freiburg', 'Augsburg'],
    "AwayTeam": ['Stuttgart', 'Leverkusen', 'Hoffenheim', 'Paderborn', "M'gladbach", 'Ein Frankfurt', 'Hamburg', 'Werder Bremen', 'Schalke 04'],
    "FTHG": [5, 3, 3, 0, 3, 3, 2, 4, 3],
    "FTAG": [1, 2, 2, 0, 0, 3, 0, 1, 0],
    "HTHG": [1, 2, 0, 0, 1, 1, 2, 2, 1],
    "HTAG": [0, 0, 1, 0, 0, 2, 0, 0, 0],
    "FTR": ['H', 'H', 'H', 'D', 'H', 'D', 'H', 'H', 'H'],
    "HTR": ['H', 'H', 'A', 'D', 'H', 'A', 'H', 'H', 'H'],
    "Date": ['28/08/26', '29/08/26', '29/08/26', '29/08/26', '29/08/26', '29/08/26', '29/08/26', '30/08/26', '30/08/26']
})

results_d2 = pd.DataFrame({
    "HomeTeam": ['Stuttgart', 'Hoffenheim', 'Leverkusen', "M'gladbach", 'Paderborn', 'Werder Bremen', 'Schalke 04', 'Hamburg', 'Ein Frankfurt'],
    "AwayTeam": ['FC Koln', 'Dortmund', 'Union Berlin', 'Elversberg', 'Freiburg', 'RB Leipzig', 'Bayern Munich', 'Mainz', 'Augsburg'],
    "FTHG": [4, 2, 4, 3, 0, 3, 0, 0, 1],
    "FTAG": [1, 3, 0, 4, 1, 1, 0, 5, 4],
    "HTHG": [1, 1, 2, 2, 0, 1, 0, 0, 1],
    "HTAG": [0, 0, 0, 1, 1, 0, 0, 2, 0],
    "FTR": ['H', 'A', 'H', 'A', 'A', 'H', 'D', 'A', 'A'],
    "HTR": ['H', 'H', 'H', 'H', 'A', 'H', 'D', 'A', 'H'],
    "Date": ['04/09/26', '05/09/26', '05/09/26', '05/09/26', '05/09/26', '05/09/26', '05/09/26', '06/09/26', '06/09/26']
})

results_d3 = pd.DataFrame({
    "HomeTeam": ['Union Berlin', 'Augsburg', 'Dortmund', 'Freiburg', 'Hoffenheim', 'Mainz', 'FC Koln', 'RB Leipzig', 'Elversberg'],
    "AwayTeam": ['Schalke 04', 'Leverkusen', 'Paderborn', "M'gladbach", 'Stuttgart', 'Ein Frankfurt', 'Werder Bremen', 'Hamburg', 'Bayern Munich'],
    "FTHG": [1, 2, 3, 5, 2, 1, 1, 5, 1],
    "FTAG": [3, 2, 0, 0, 1, 3, 1, 0, 2],
    "HTHG": [0, 0, 1, 2, 1, 0, 1, 2, 0],
    "HTAG": [1, 1, 0, 0, 0, 2, 0, 0, 1],
    "FTR": ['A', 'D', 'H', 'H', 'H', 'A', 'D', 'H', 'A'],
    "HTR": ['A', 'A', 'H', 'H', 'H', 'A', 'H', 'H', 'A'],
    "Date": ['11/09/26', '12/09/26', '12/09/26', '12/09/26', '12/09/26', '12/09/26', '12/09/26', '13/09/26', '13/09/26']
})

results_d4 = pd.DataFrame({
    "HomeTeam": ['Bayern Munich', 'Ein Frankfurt', 'Hamburg', "M'gladbach", 'Werder Bremen', 'Stuttgart', 'Leverkusen', 'Schalke 04', 'Paderborn'],
    "AwayTeam": ['Union Berlin', 'Freiburg', 'FC Koln', 'Mainz', 'Augsburg', 'Dortmund', 'RB Leipzig', 'Elversberg', 'Hoffenheim'],
    "FTHG": [7, 2, 2, 3, 3, 0, 2, 0, 3],
    "FTAG": [0, 2, 1, 4, 2, 1, 0, 0, 1],
    "HTHG": [3, 2, 1, 1, 0, 0, 1, 0, 2],
    "HTAG": [0, 1, 0, 2, 1, 0, 0, 0, 0],
    "FTR": ['H', 'D', 'H', 'A', 'H', 'A', 'H', 'D', 'H'],
    "HTR": ['H', 'H', 'H', 'A', 'A', 'D', 'H', 'D', 'H'],
    "Date": ['18/09/26', '19/09/26', '19/09/26', '19/09/26', '19/09/26', '19/09/26', '20/09/26', '20/09/26', '20/09/26']
})

results_d5 = pd.DataFrame({
    "HomeTeam": ['Dortmund', 'Augsburg', 'Hoffenheim', 'Mainz', 'Paderborn', 'Union Berlin', 'RB Leipzig', 'FC Koln', 'Freiburg'],
    "AwayTeam": ['Werder Bremen', 'Bayern Munich', 'Hamburg', 'Leverkusen', 'Stuttgart', 'Elversberg', 'Ein Frankfurt', "M'gladbach", 'Schalke 04'],
    "FTHG": [2, 2, 2, 3, 0, 1, 6, 2, 2],
    "FTAG": [2, 2, 3, 4, 2, 0, 0, 1, 1],
    "HTHG": [0, 1, 1, 2, 0, 0, 4, 1, 1],
    "HTAG": [0, 0, 1, 2, 1, 0, 0, 1, 1],
    "FTR": ['D', 'D', 'A', 'A', 'A', 'H', 'H', 'H', 'H'],
    "HTR": ['D', 'H', 'D', 'D', 'A', 'D', 'H', 'D', 'D'],
    "Date": ['09/10/26', '10/10/26', '10/10/26', '10/10/26', '10/10/26', '10/10/26', '10/10/26', '11/10/26', '11/10/26']
})

results_d6 = pd.DataFrame({
    "HomeTeam": ['Ein Frankfurt', 'Elversberg', 'Hamburg', 'Schalke 04', 'Union Berlin', 'Werder Bremen', 'Bayern Munich', 'Leverkusen', "M'gladbach"],
    "AwayTeam": ['FC Koln', 'Augsburg', 'Stuttgart', 'Mainz', 'Dortmund', 'Paderborn', 'RB Leipzig', 'Freiburg', 'Hoffenheim'],
    "FTHG": [1, 4, 1, 0, 0, 2, 6, 2, 1],
    "FTAG": [0, 3, 0, 1, 0, 2, 1, 1, 2],
    "HTHG": [0, 3, 0, 0, 0, 0, 3, 1, 0],
    "HTAG": [0, 1, 0, 1, 0, 2, 0, 1, 1],
    "FTR": ['H', 'H', 'H', 'A', 'D', 'D', 'H', 'H', 'A'],
    "HTR": ['D', 'H', 'D', 'A', 'D', 'A', 'H', 'D', 'A'],
    "Date": ['16/10/26', '17/10/26', '17/10/26', '17/10/26', '17/10/26', '17/10/26', '17/10/26', '18/10/26', '18/10/26']
})

results_d7 = pd.DataFrame({
    "HomeTeam": ['Stuttgart', 'Augsburg', 'FC Koln', 'Mainz', 'Paderborn', 'RB Leipzig', 'Dortmund', 'Hoffenheim', 'Freiburg'],
    "AwayTeam": ["M'gladbach", 'Union Berlin', 'Schalke 04', 'Werder Bremen', 'Hamburg', 'Elversberg', 'Ein Frankfurt', 'Leverkusen', 'Bayern Munich'],
    "FTHG": [2, 1, 0, 2, 1, 4, 1, 3, 1],
    "FTAG": [3, 1, 0, 3, 0, 0, 0, 0, 3],
    "HTHG": [1, 0, 0, 1, 0, 0, 0, 0, 0],
    "HTAG": [1, 0, 0, 2, 0, 0, 0, 0, 2],
    "FTR": ['A', 'D', 'D', 'A', 'H', 'H', 'H', 'H', 'A'],
    "HTR": ['D', 'D', 'D', 'A', 'D', 'D', 'D', 'D', 'A'],
    "Date": ['23/10/26', '24/10/26', '24/10/26', '24/10/26', '24/10/26', '24/10/26', '24/10/26', '25/10/26', '25/10/26']
})

results_d8 = pd.DataFrame({
    "HomeTeam": ['Elversberg', 'Augsburg', 'Leverkusen', "M'gladbach", 'Schalke 04', 'Werder Bremen', 'Bayern Munich', 'Union Berlin', 'Ein Frankfurt'],
    "AwayTeam": ['Mainz', 'Freiburg', 'Stuttgart', 'Paderborn', 'RB Leipzig', 'Hoffenheim', 'Dortmund', 'FC Koln', 'Hamburg'],
    "FTHG": [4, 1, 2, 0, 0, 2, 2, 1, 3],
    "FTAG": [1, 2, 4, 0, 2, 0, 2, 1, 1],
    "HTHG": [3, 1, 1, 0, 0, 0, 1, 1, 1],
    "HTAG": [0, 0, 2, 0, 1, 0, 0, 0, 1],
    "FTR": ['H', 'A', 'A', 'D', 'A', 'H', 'D', 'D', 'H'],
    "HTR": ['H', 'H', 'A', 'D', 'A', 'D', 'H', 'H', 'D'],
    "Date": ['30/10/26', '31/10/26', '31/10/26', '31/10/26', '31/10/26', '31/10/26', '31/10/26', '01/11/26', '01/11/26']
})

results_d9 = pd.DataFrame({
    "HomeTeam": ['Hamburg', 'Dortmund', 'Mainz', 'Paderborn', 'RB Leipzig', 'Stuttgart', 'FC Koln', 'Freiburg', 'Hoffenheim'],
    "AwayTeam": ["M'gladbach", 'Elversberg', 'Bayern Munich', 'Ein Frankfurt', 'Augsburg', 'Werder Bremen', 'Leverkusen', 'Union Berlin', 'Schalke 04'],
    "FTHG": [3, 2, 1, 2, 5, 1, 1, 2, 2],
    "FTAG": [1, 1, 2, 2, 2, 0, 2, 0, 1],
    "HTHG": [1, 0, 0, 1, 3, 1, 0, 0, 2],
    "HTAG": [1, 0, 1, 1, 1, 0, 1, 0, 0],
    "FTR": ['H', 'H', 'A', 'D', 'H', 'H', 'A', 'H', 'H'],
    "HTR": ['D', 'D', 'A', 'D', 'H', 'H', 'A', 'D', 'H'],
    "Date": ['06/11/26', '07/11/26', '07/11/26', '07/11/26', '07/11/26', '07/11/26', '08/11/26', '08/11/26', '08/11/26']
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
