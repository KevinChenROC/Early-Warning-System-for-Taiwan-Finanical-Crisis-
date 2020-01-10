import pandas as pd
import numpy as np


def calc_simple_rates(series):  # return a series with the same indexes.
    start_index = 0

    # find the index of first non-NaN
    for i in range(start_index, series.size):
        if(not np.isnan(series[i])):
            start_index = i+1
            break

    rates = []
    for i in range(start_index, series.size):
        if(np.isclose(series[i-1], 0)):
            rate = 0
        else:
            rate = series[i]/series[i-1] - 1
        rates.append(rate)

    return pd.Series(rates, index=series.index[start_index:]).dropna()
