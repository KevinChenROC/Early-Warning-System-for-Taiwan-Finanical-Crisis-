import pandas as pd
import numpy as np

from .calc_rate import calc_simple_rates
from .stats import ecdf


def get_crisis_label(change_rates, return_distr_window, market_crash_threshold):
    """
    change_rates: pd.Series
    return Pandas.Dataframe
    """
    change_rates = change_rates.dropna()

    start_idx = return_distr_window
    df = pd.DataFrame(index=change_rates.index, columns=['Crisis'])

    for i in range(start_idx, change_rates.size):
        percentile = ecdf(change_rates[:i].to_numpy(), change_rates[i].item())
        if(percentile < market_crash_threshold):
            df.at[df.index[i], 'Crisis'] = 1
        else:
            df.at[df.index[i], 'Crisis'] = 0

    return df.dropna()
