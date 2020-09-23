"""
This can be used like so:

import hard_coded_method as hcm

predictions = hcm.predict(filename='new_loan_data.csv')
"""
import pandas as pd
import swifter


def screen(x):
    if 'High Risk' in x['PERFORM_CNS_SCORE_DESCRIPTION']:
        return 1
    elif 'Medium Risk' in x['PERFORM_CNS_SCORE_DESCRIPTION'] and x['LTV'] > 70:
        return 1
    elif 'Not Scored' in x['PERFORM_CNS_SCORE_DESCRIPTION'] and x['LTV'] > 70:
        return 1
    else:
        return 0


def score_risk(filename):
    # load file and keep only used columns
    df = pd.read_csv(filename)
    keep_columns = ['UNIQUEID',
                    'LTV',
                    'PERFORM_CNS_SCORE_DESCRIPTION',
                    'LOAN_DEFAULT']
    df = df[keep_columns]

    # create default risk column and screen based on our rules, then return that column
    df['DEFAULT_RISK'] = 0
    df['DEFAULT_RISK'] = df.swifter.apply(lambda x: screen(x), axis=1)
    return df[['UNIQUEID', 'DEFAULT_RISK']]
