import pandas as pd

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
    "AwayTeam": ['FC Koln', 'Heidenheim', 'Hoffenheim', 'Wolfsburg', 'Werder Bremen', 'Freiburg', 'Dortmund',
                 'Ein Frankfurt'],
    "FTHG": [0, 2, 2, 3, 2, 0, 1, 2],
    "FTAG": [1, 1, 1, 1, 0, 1, 1, 1],
    "HTHG": [0, 2, 0, 2, 1, 0, 0, 1],
    "HTAG": [0, 1, 0, 1, 0, 0, 1, 0],
    "FTR": ['A', 'H', 'H', 'H', 'H', 'A', 'D', 'H'],
    "HTR": ['D', 'H', 'D', 'H', 'H', 'D', 'A', 'H'],
    "Date": ['01/12/23', '02/12/23', '02/12/23', '02/12/23', '02/12/23', '03/12/23', '03/12/23', '03/12/23']
})
results_d14 = pd.DataFrame({
    "HomeTeam": ['Hoffenheim', 'Wolfsburg', 'Heidenheim', 'Union Berlin', 'Werder Bremen', 'Ein Frankfurt', 'Dortmund',
                 'Stuttgart', 'FC Koln'],
    "AwayTeam": ['Bochum', 'Freiburg', 'Darmstadt', "M'gladbach", 'Augsburg', 'Bayern Munich', 'RB Leipzig',
                 'Leverkusen', 'Mainz'],
    "FTHG": [3, 0, 3, 3, 2, 5, 2, 1, 0],
    "FTAG": [1, 1, 2, 1, 0, 1, 3, 1, 0],
    "HTHG": [2, 0, 1, 1, 1, 3, 1, 1, 0],
    "HTAG": [0, 0, 0, 0, 0, 1, 1, 0, 0],
    "FTR": ['H', 'A', 'H', 'H', 'H', 'H', 'A', 'D', 'D'],
    "HTR": ['H', 'D', 'H', 'H', 'H', 'H', 'D', 'H', 'D'],
    "Date": ['08/12/23', '09/12/23', '09/12/23', '09/12/23', '09/12/23', '09/12/23', '09/12/23', '10/12/23', '10/12/23']
})
results_d15 = pd.DataFrame({
    "HomeTeam": ["M'gladbach", 'Mainz', 'Bochum', 'Augsburg', 'Darmstadt', 'RB Leipzig', 'Freiburg', 'Leverkusen',
                 'Bayern Munich'],
    "AwayTeam": ['Werder Bremen', 'Heidenheim', 'Union Berlin', 'Dortmund', 'Wolfsburg', 'Hoffenheim', 'FC Koln',
                 'Ein Frankfurt', 'Stuttgart'],
    "FTHG": [2, 0, 3, 1, 0, 3, 2, 3, 3],
    "FTAG": [2, 1, 0, 1, 1, 1, 0, 0, 0],
    "HTHG": [1, 0, 1, 1, 0, 1, 0, 1, 1],
    "HTAG": [1, 1, 0, 1, 0, 1, 0, 0, 0],
    "FTR": ['D', 'A', 'H', 'D', 'A', 'H', 'H', 'H', 'H'],
    "HTR": ['D', 'A', 'H', 'D', 'D', 'D', 'D', 'H', 'H'],
    "Date": ['15/12/23', '16/12/23', '16/12/23', '16/12/23', '16/12/23', '16/12/23', '17/12/23', '17/12/23', '17/12/23']
})
results_d16 = pd.DataFrame({
    "HomeTeam": ['Werder Bremen', 'Dortmund', 'Hoffenheim', 'Union Berlin', 'Leverkusen', 'Stuttgart', 'Wolfsburg',
                 'Heidenheim', 'Ein Frankfurt'],
    "AwayTeam": ['RB Leipzig', 'Mainz', 'Darmstadt', 'FC Koln', 'Bochum', 'Augsburg', 'Bayern Munich', 'Freiburg',
                 "M'gladbach"],
    "FTHG": [1, 1, 3, 2, 4, 3, 1, 3, 2],
    "FTAG": [1, 1, 3, 0, 0, 0, 2, 2, 1],
    "HTHG": [0, 1, 2, 0, 3, 2, 1, 0, 0],
    "HTAG": [0, 1, 1, 0, 0, 0, 2, 1, 1],
    "FTR": ['D', 'D', 'D', 'H', 'H', 'H', 'A', 'H', 'H'],
    "HTR": ['D', 'D', 'H', 'D', 'H', 'H', 'A', 'A', 'A'],
    "Date": ['19/12/23', '19/12/23', '19/12/23', '20/12/23', '20/12/23', '20/12/23', '20/12/23', '20/12/23', '20/12/23']
})
results_d17 = pd.DataFrame({
    "HomeTeam": ['Bayern Munich', 'Mainz', 'Augsburg', 'FC Koln', 'RB Leipzig', 'Freiburg', 'Darmstadt', 'Bochum', "M'gladbach"],
    "AwayTeam": ['Hoffenheim', 'Wolfsburg', 'Leverkusen', 'Heidenheim', 'Ein Frankfurt', 'Union Berlin', 'Dortmund', 'Werder Bremen', 'Stuttgart'],
    "FTHG": [3, 1, 0, 1, 0, 0, 0, 1, 3],
    "FTAG": [0, 1, 1, 1, 1, 0, 3, 1, 1],
    "HTHG": [1, 0, 0, 1, 0, 0, 0, 0, 2],
    "HTAG": [0, 1, 0, 0, 1, 0, 1, 0, 0],
    "FTR": ['H', 'D', 'A', 'D', 'A', 'D', 'A', 'D', 'H'],
    "HTR": ['H', 'A', 'D', 'H', 'A', 'D', 'A', 'D', 'H'],
    "Date": ['12/01/24', '13/01/24', '13/01/24', '13/01/24', '13/01/24', '13/01/24', '13/01/24', '14/01/24', '14/01/24']
})
results_d18 = pd.DataFrame({
    "HomeTeam": ['Darmstadt', 'Freiburg', 'Bochum', 'Heidenheim', 'FC Koln', 'RB Leipzig', 'Bayern Munich', "M'gladbach"],
    "AwayTeam": ['Ein Frankfurt', 'Hoffenheim', 'Stuttgart', 'Wolfsburg', 'Dortmund', 'Leverkusen', 'Werder Bremen', 'Augsburg'],
    "FTHG": [2, 3, 1, 1, 0, 2, 0, 1],
    "FTAG": [2, 2, 0, 1, 4, 3, 1, 2],
    "HTHG": [0, 1, 0, 1, 0, 1, 0, 1],
    "HTAG": [1, 0, 0, 1, 1, 0, 0, 0],
    "FTR": ['A', 'H', 'D', 'D', 'A', 'H', 'D', 'H'],
    "HTR": ['D', 'H', 'H', 'D', 'A', 'A', 'A', 'A'],
    "Date": ['20/01/24', '20/01/24', '20/01/24', '20/01/24', '20/01/24', '20/01/24', '21/01/24', '21/01/24',]
})
results_d19 = pd.DataFrame({
    "HomeTeam": ['Ein Frankfurt', 'Stuttgart', 'Hoffenheim', 'Wolfsburg', 'Augsburg', 'Werder Bremen', 'Leverkusen', 'Union Berlin', 'Dortmund'],
    "AwayTeam": ['Mainz', 'RB Leipzig', 'Heidenheim', 'FC Koln', 'Bayern Munich', 'Freiburg', "M'gladbach", 'Darmstadt', 'Bochum'],
    "FTHG": [1, 5, 1, 1, 2, 3, 0, 1, 3],
    "FTAG": [0, 2, 1, 1, 3, 1, 0, 0, 1],
    "HTHG": [0, 2, 1, 1, 0, 1, 0, 0, 1],
    "HTAG": [0, 1, 1, 1, 2, 1, 0, 0, 1],
    "FTR": ['H', 'H', 'D', 'D', 'A', 'H', 'D', 'H', 'H'],
    "HTR": ['D', 'H', 'D', 'D', 'A', 'D', 'D', 'D', 'D'],
    "Date": ['26/01/24', '27/01/24', '27/01/24', '27/01/24', '27/01/24', '27/01/24', '27/01/24', '28/01/24', '28/01/24',]
})
results_d20 = pd.DataFrame({
    "HomeTeam": ['Heidenheim', 'Bayern Munich', 'Darmstadt', 'Freiburg', 'Mainz', 'Bochum', 'FC Koln', 'Wolfsburg', 'RB Leipzig'],
    "AwayTeam": ['Dortmund', "M'gladbach", 'Leverkusen', 'Stuttgart', 'Werder Bremen', 'Augsburg', 'Ein Frankfurt', 'Hoffenheim', 'Union Berlin'],
    "FTHG": [0, 3, 0, 1, 0, 1, 2, 2, 2],
    "FTAG": [0, 1, 2, 3, 1, 1, 0, 2, 0],
    "HTHG": [0, 1, 0, 1, 0, 1, 0, 0, 1],
    "HTAG": [0, 1, 1, 2, 1, 0, 0, 1, 0],
    "FTR": ['D', 'H', 'A', 'A', 'A', 'D', 'H', 'D', 'H'],
    "HTR": ['D', 'D', 'A', 'A', 'A', 'H', 'D', 'A', 'H'],
    "Date": ['02/02/24', '02/02/24', '03/02/24', '03/02/24', '03/02/24', '03/02/24', '03/02/24', '04/02/24', '04/02/24']
})
results_d21 = pd.DataFrame({
    "HomeTeam": ['Dortmund', 'Union Berlin', 'Ein Frankfurt', 'Werder Bremen', 'Augsburg', "M'gladbach", 'Leverkusen', 'Stuttgart', 'Hoffenheim'],
    "AwayTeam": ['Freiburg', 'Wolfsburg', 'Bochum', 'Heidenheim', 'RB Leipzig', 'Darmstadt', 'Bayern Munich', 'Mainz', 'FC Koln'],
    "FTHG": [3, 1, 1, 1, 2, 0, 3, 3, 1],
    "FTAG": [0, 0, 1, 2, 2, 0, 0, 1, 1],
    "HTHG": [2, 1, 1, 1, 1, 0, 1, 2, 0],
    "HTAG": [0, 0, 1, 2, 1, 0, 0, 0, 0],
    "FTR": ['H', 'H', 'D', 'A', 'D', 'D', 'H', 'H', 'D'],
    "HTR": ['H', 'H', 'D', 'A', 'D', 'D', 'H', 'H', 'D'],
    "Date": ['09/02/24', '10/02/24', '10/02/24', '10/02/24', '10/02/24', '10/02/24', '10/02/24', '11/02/24', '11/02/24']
})
results_d22 = pd.DataFrame({
    "HomeTeam": ['FC Koln', 'Hoffenheim', 'Heidenheim', 'Darmstadt', 'Wolfsburg', 'Mainz', 'RB Leipzig', 'Freiburg', 'Bochum'],
    "AwayTeam": ['Werder Bremen', 'Union Berlin', 'Leverkusen', 'Stuttgart', 'Dortmund', 'Augsburg', "M'gladbach", 'Ein Frankfurt', 'Bayern Munich'],
    "FTHG": [0, 0, 1, 1, 1, 1, 2, 3, 3],
    "FTAG": [1, 1, 2, 2, 1, 0, 0, 3, 2],
    "HTHG": [0, 0, 0, 0, 0, 1, 1, 2, 2],
    "HTAG": [0, 0, 1, 1, 1, 0, 0, 2, 1],
    "FTR": ['A', 'A', 'A', 'A', 'D', 'H', 'H', 'D', 'H'],
    "HTR": ['D', 'D', 'A', 'A', 'A', 'H', 'H', 'D', 'H'],
    "Date": ['16/02/24', '17/02/24', '17/02/24', '17/02/24', '17/02/24', '17/02/24', '17/02/24', '18/02/24', '18/02/24']
})
results_d23 = pd.DataFrame({
    "HomeTeam": ['Leverkusen', "M'gladbach", 'Union Berlin', 'Stuttgart', 'Werder Bremen', 'Bayern Munich', 'Ein Frankfurt', 'Dortmund', 'Augsburg'],
    "AwayTeam": ['Mainz', 'Bochum', 'Heidenheim', 'FC Koln', 'Darmstadt', 'RB Leipzig', 'Wolfsburg', 'Hoffenheim', 'Freiburg'],
    "FTHG": [2, 5, 2, 1, 1, 2, 2, 2, 2],
    "FTAG": [1, 2, 2, 1, 1, 1, 2, 3, 1],
    "HTHG": [1, 2, 2, 0, 1, 0, 1, 2, 0],
    "HTAG": [1, 0, 1, 0, 1, 0, 2, 1, 1],
    "FTR": ['H', 'H', 'D', 'D', 'D', 'H', 'D', 'A', 'H'],
    "HTR": ['A', 'H', 'H', 'D', 'D', 'D', 'A', 'H', 'A'],
    "Date": ['23/02/24', '24/02/24', '24/02/24', '24/02/24', '24/02/24', '24/02/24', '25/02/24', '25/02/24', '25/02/24']
})

results_d24 = pd.DataFrame({
    "HomeTeam": ['Freiburg', 'Heidenheim', 'Mainz', 'Bochum', 'Darmstadt', 'Union Berlin', 'Wolfsburg', 'FC Koln', 'Hoffenheim'],
    "AwayTeam": ['Bayern Munich', 'Ein Frankfurt', "M'gladbach", 'RB Leipzig', 'Augsburg', 'Dortmund', 'Stuttgart', 'Leverkusen', 'Werder Bremen'],
    "FTHG": [2, 1, 1, 1, 0, 0, 2, 0, 2],
    "FTAG": [2, 2, 1, 4, 6, 2, 3, 2, 1],
    "HTHG": [1, 0, 1, 1, 0, 0, 0, 0, 2],
    "HTAG": [1, 1, 0, 1, 5, 1, 1, 1, 0],
    "FTR": ['D', 'A', 'D', 'A', 'A', 'A', 'A', 'A', 'H'],
    "HTR": ['D', 'A', 'H', 'D', 'A', 'A', 'A', 'A', 'H'],
    "Date": ['01/03/24', '02/03/24', '02/03/24', '02/03/24', '02/03/24', '02/03/24', '02/03/24', '03/03/24', '03/03/24',]
})

results_d25 = pd.DataFrame({
    "HomeTeam": ['Stuttgart', "M'gladbach", 'Augsburg', 'RB Leipzig', 'Bayern Munich', 'Werder Bremen', 'Bochum', 'Ein Frankfurt', 'Leverkusen'],
    "AwayTeam": ['Union Berlin', 'FC Koln', 'Heidenheim', 'Darmstadt', 'Mainz', 'Dortmund', 'Freiburg', 'Hoffenheim', 'Wolfsburg'],
    "FTHG": [2, 3, 1, 2, 8, 1, 1, 3, 2],
    "FTAG": [0, 3, 0, 0, 1, 2, 2, 1, 0],
    "HTHG": [1, 1, 1, 1, 3, 0, 0, 1, 1],
    "HTAG": [0, 1, 0, 0, 1, 2, 1, 1, 0],
    "FTR": ['H', 'D', 'H', 'H', 'H', 'A', 'A', 'H', 'H'],
    "HTR": ['H', 'D', 'H', 'H', 'H', 'A', 'A', 'A', 'H'],
    "Date": ['08/03/24', '09/03/24', '09/03/24', '09/03/24', '09/03/24', '09/03/24', '10/03/24', '10/03/24', '10/03/24']
})

results_d26 = pd.DataFrame({
    "HomeTeam": ['FC Koln', 'Union Berlin', 'Darmstadt', 'Wolfsburg', 'Mainz', 'Heidenheim', 'Hoffenheim', 'Freiburg', 'Dortmund'],
    "AwayTeam": ['RB Leipzig', 'Werder Bremen', 'Bayern Munich', 'Augsburg', 'Bochum', "M'gladbach", 'Stuttgart', 'Leverkusen', 'Ein Frankfurt'],
    "FTHG": [1, 2, 2, 1, 2, 1, 0, 2, 3],
    "FTAG": [5, 1, 5, 3, 0, 1, 3, 3, 1],
    "HTHG": [1, 0, 1, 1, 1, 0, 0, 1, 1],
    "HTAG": [1, 0, 2, 1, 0, 1, 2, 2, 1],
    "FTR": ['A', 'H', 'A', 'A', 'H', 'D', 'A', 'A', 'H'],
    "HTR": ['D', 'D', 'A', 'D', 'H', 'A', 'A', 'A', 'D'],
    "Date": ['15/03/24', '16/03/24', '16/03/24', '16/03/24', '16/03/24', '16/03/24', '16/03/24', '17/03/24', '17/03/24']
})

results_d27 = pd.DataFrame({
    "HomeTeam": ["M'gladbach", 'Leverkusen', 'Werder Bremen', 'RB Leipzig', 'Ein Frankfurt', 'Bayern Munich', 'Augsburg', 'Stuttgart', 'Bochum'],
    "AwayTeam": ['Freiburg', 'Hoffenheim', 'Wolfsburg', 'Mainz', 'Union Berlin', 'Dortmund', 'FC Koln', 'Heidenheim', 'Darmstadt'],
    "FTHG": [0, 2, 0, 0, 0, 0, 1, 3, 2],
    "FTAG": [3, 1, 2, 0, 0, 2, 1, 3, 2],
    "HTHG": [0, 0, 0, 0, 0, 0, 1, 1, 1],
    "HTAG": [1, 1, 1, 0, 0, 1, 1, 0, 0],
    "FTR": ['A', 'H', 'A', 'D', 'D', 'A', 'D', 'D', 'D'],
    "HTR": ['A', 'A', 'A', 'D', 'D', 'A', 'D', 'H', 'H'],
    "Date": ['30/03/24', '30/03/24', '30/03/24', '30/03/24', '30/03/24', '30/03/24', '31/03/24', '31/03/24', '31/03/24']
})

results_d28 = pd.DataFrame({
    "HomeTeam": ['Ein Frankfurt', 'Freiburg', 'Union Berlin', 'FC Koln', 'Heidenheim', 'Mainz', 'Dortmund', 'Hoffenheim', 'Wolfsburg'],
    "AwayTeam": ['Werder Bremen', 'RB Leipzig', 'Leverkusen', 'Bochum', 'Bayern Munich', 'Darmstadt', 'Stuttgart', 'Augsburg', "M'gladbach"],
    "FTHG": [1, 1, 0, 2, 3, 4, 0, 3, 1],
    "FTAG": [1, 4, 1, 1, 2, 0, 1, 1, 3],
    "HTHG": [0, 0, 0, 0, 0, 1, 0, 2, 1],
    "HTAG": [0, 3, 1, 0, 2, 0, 0, 0, 0],
    "FTR": ['D', 'A', 'A', 'H', 'H', 'H', 'A', 'H', 'A'],
    "HTR": ['D', 'A', 'A', 'D', 'A', 'H', 'D', 'H', 'H'],
    "Date": ['05/04/24', '06/04/24', '06/04/24', '06/04/24', '06/04/24', '06/04/24', '06/04/24', '07/04/24', '07/04/24']
})

results_d29 = pd.DataFrame({
    "HomeTeam": ['Augsburg', 'Mainz', 'RB Leipzig', 'Bayern Munich', 'Bochum', "M'gladbach", 'Stuttgart', 'Darmstadt', 'Leverkusen'],
    "AwayTeam": ['Union Berlin', 'Hoffenheim', 'Wolfsburg', 'FC Koln', 'Heidenheim', 'Dortmund', 'Ein Frankfurt', 'Freiburg', 'Werder Bremen'],
    "FTHG": [2, 4, 3, 2, 1, 1, 3, 0, 5],
    "FTAG": [0, 1, 0, 0, 1, 2, 0, 1, 0],
    "HTHG": [0, 0, 1, 0, 0, 1, 3, 0, 1],
    "HTAG": [0, 1, 0, 0, 0, 2, 0, 1, 0],
    "FTR": ['H', 'H', 'H', 'H', 'D', 'A', 'H', 'A', 'H'],
    "HTR": ['D', 'A', 'H', 'D', 'D', 'A', 'H', 'A', 'H'],
    "Date": ['12/04/24', '13/04/24', '13/04/24', '13/04/24', '13/04/24', '13/04/24', '13/04/24', '14/04/24', '14/04/24']
})

results_d30 = pd.DataFrame({
    "HomeTeam": ['Ein Frankfurt', 'Wolfsburg', 'Heidenheim', 'Hoffenheim', 'FC Koln', 'Union Berlin', 'Werder Bremen', 'Dortmund', 'Freiburg'],
    "AwayTeam": ['Augsburg', 'Bochum', 'RB Leipzig', "M'gladbach", 'Darmstadt', 'Bayern Munich', 'Stuttgart', 'Leverkusen', 'Mainz'],
    "FTHG": [3, 1, 1, 4, 0, 1, 2, 1, 1],
    "FTAG": [1, 0, 2, 3, 2, 5, 1, 1, 1],
    "HTHG": [0, 1, 0, 1, 0, 0, 1, 0, 1],
    "HTAG": [1, 0, 1, 1, 0, 2, 0, 0, 1],
    "FTR": ['A', 'H', 'A', 'H', 'A', 'A', 'H', 'D', 'D'],
    "HTR": ['H', 'H', 'A', 'D', 'D', 'A', 'H', 'D', 'D'],
    "Date": ['19/04/24', '20/04/24', '20/04/24', '20/04/24', '20/04/24', '20/04/24', '21/04/24', '21/04/24', '21/04/24',]
})

results_d31 = pd.DataFrame({
    "HomeTeam": ['Bochum', 'Bayern Munich', 'RB Leipzig', 'Augsburg', 'Freiburg', 'Leverkusen', "M'gladbach", 'Mainz', 'Darmstadt'],
    "AwayTeam": ['Hoffenheim', 'Ein Frankfurt', 'Dortmund', 'Werder Bremen', 'Wolfsburg', 'Stuttgart', 'Union Berlin', 'FC Koln', 'Heidenheim'],
    "FTHG": [3, 2, 4, 0, 1, 2, 0, 1, 0],
    "FTAG": [2, 1, 1, 3, 2, 2, 0, 1, 1],
    "HTHG": [2, 1, 2, 0, 1, 0, 0, 1, 0],
    "HTAG": [0, 1, 1, 0, 0, 0, 0, 0, 0],
    "FTR": ['H', 'H', 'H', 'A', 'A', 'D', 'D', 'D', 'A'],
    "HTR": ['H', 'D', 'H', 'D', 'H', 'D', 'D', 'H', 'D'],
    "Date": ['26/04/24', '27/04/24', '27/04/24', '27/04/24', '27/04/24', '27/04/24', '28/04/24', '28/04/24', '28/04/24',]
})

results_d32 = pd.DataFrame({
    "HomeTeam": ['Hoffenheim', 'Dortmund', 'Wolfsburg', 'Stuttgart', 'Werder Bremen', 'FC Koln', 'Union Berlin', 'Ein Frankfurt', 'Heidenheim'],
    "AwayTeam": ['RB Leipzig', 'Augsburg', 'Darmstadt', 'Bayern Munich', "M'gladbach", 'Freiburg', 'Bochum', 'Leverkusen', 'Mainz'],
    "FTHG": [1, 5, 3, 3, 2, 0, 3, 1, 1],
    "FTAG": [1, 1, 0, 1, 2, 0, 4, 5, 1],
    "HTHG": [0, 4, 2, 1, 1, 0, 0, 1, 0],
    "HTAG": [1, 1, 0, 1, 1, 0, 3, 2, 1],
    "FTR": ['D', 'H', 'H', 'H', 'D', 'D', 'A', 'A', 'D'],
    "HTR": ['A', 'H', 'H', 'D', 'D', 'D', 'A', 'A', 'A'],
    "Date": ['03/05/24', '04/05/24', '04/05/24', '04/05/24', '04/05/24', '04/05/24', '05/05/24', '05/05/24', '05/05/24']
})

results_d33 = pd.DataFrame({
    "HomeTeam": ['Augsburg', 'FC Koln', "M'gladbach", 'Freiburg', 'RB Leipzig', 'Mainz', 'Darmstadt', 'Bayern Munich', 'Bochum'],
    "AwayTeam": ['Stuttgart', 'Union Berlin', 'Ein Frankfurt', 'Heidenheim', 'Werder Bremen', 'Dortmund', 'Hoffenheim', 'Wolfsburg', 'Leverkusen'],
    "FTHG": [0, 3, 1, 1, 1, 3, 0, 2, 0],
    "FTAG": [1, 2, 1, 1, 1, 0, 6, 0, 5],
    "HTHG": [0, 1, 1, 1, 0, 3, 0, 2, 0],
    "HTAG": [0, 2, 1, 1, 1, 0, 5, 0, 2],
    "FTR": ['A', 'H', 'D', 'D', 'D', 'H', 'A', 'H', 'A'],
    "HTR": ['D', 'A', 'D', 'D', 'A', 'H', 'A', 'H', 'A'],
    "Date": ['10/05/24', '11/05/24', '11/05/24', '11/05/24', '11/05/24', '11/05/24', '12/05/24', '12/05/24', '12/05/24']
})

results_d34 = pd.DataFrame({
    "HomeTeam": ['Stuttgart', 'Leverkusen', 'Heidenheim', 'Dortmund', 'Werder Bremen', 'Union Berlin', 'Wolfsburg', 'Hoffenheim', 'Ein Frankfurt'],
    "AwayTeam": ["M'gladbach", 'Augsburg', 'FC Koln', 'Darmstadt', 'Bochum', 'Freiburg', 'Mainz', 'Bayern Munich', 'RB Leipzig'],
    "FTHG": [4, 2, 4, 4, 4, 2, 1, 4, 2],
    "FTAG": [0, 1, 1, 0, 1, 1, 3, 2, 2],
    "HTHG": [2, 2, 3, 2, 1, 0, 1, 1, 0],
    "HTAG": [0, 0, 0, 0, 0, 0, 1, 2, 1],
    "FTR": ['H', 'H', 'H', 'H', 'H', 'H', 'A', 'A', 'D'],
    "HTR": ['H', 'H', 'H', 'H', 'H', 'D', 'D', 'H', 'A'],
    "Date": ['18/05/24', '18/05/24', '18/05/24', '18/05/24', '18/05/24', '18/05/24', '18/05/24', '18/05/24', '18/05/24']
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