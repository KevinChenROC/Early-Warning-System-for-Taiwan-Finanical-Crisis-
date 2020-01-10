import os
from os.path import isfile, join

import pandas as pd
import numpy as np

from data_transform.util.calc_rate import *
from data_transform.util.file_extension import *


def get_file_names(dir_path):
    file_names = [f for f in os.listdir(
        dir_path) if isfile(join(dir_path, f))]
    return file_names


def get_change_rates(series, symbol, fill_freq):
    series = calc_simple_rates(series)

    # back fill missing values
    series = series.asfreq(freq=fill_freq, method='bfill')
    return series.to_frame(name=symbol)


# Merge datas in a folder in raw data
def merge_data_in_folder(data_dir, value_col, start_date, end_date, fill_freq='1D'):
    """
    return: dataframe with missing values forward filled
    """

    time_indexes = pd.date_range(start_date, end_date, freq='1D')
    target_df = pd.DataFrame(index=time_indexes)

    for f in get_file_names(data_dir):
        df = pd.read_csv(data_dir+f,
                         header=0, parse_dates=[0], index_col=0)

        # transform data
        df = get_change_rates(
            df[value_col], remove_extension(f), fill_freq)

        # merge dataframes. Do left join then ffill
        target_df = target_df.join(df, how="left").fillna(method='ffill')

    return target_df.dropna()


# Merge datasets from different folders
def merge_datasets(paths, value_columns, start_date, end_date):
    """

    param types: list, list, list
    return pandas.datafraem

    """
    merge_df = pd.DataFrame()
    for i in range(0, len(paths)):
        df = merge_data_in_folder(
            paths[i], value_columns[i],  start_date, end_date)

        if(merge_df.empty):
            merge_df = df
        else:
            merge_df = merge_df.merge(df, left_index=True,
                                      right_index=True, how='inner')
    return merge_df
