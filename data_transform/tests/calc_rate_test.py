import pandas as pd
import numpy as np

from ..util.calc_rate import calc_simple_rates


def run_tests():
    df = pd.read_csv("datasets/raw_data/bond_yield_indexes/TGBRATE.csv",
                     header=0, parse_dates=[0], index_col=0)
    df["Change rate"] = calc_simple_rates(df['Value'])
    df = df.dropna()

    for i in range(1, int(len(df)/2)):
        assert df.at[df.index[i], 'Change rate'] == (
            df.iat[i, 0]/df.iat[i-1, 0]-1)
