import os
from os.path import isfile, join

import pandas as pd

from .utils.url_maker import make_url_stock_ai
from .utils.download_helper import download_file


def download_raw_data(symbols_folder_path, raw_data_folder_path, data_start_date, data_end_date, r_key):
    # iterate through all csvs of symbols
    symbols_file_paths = [f for f in os.listdir(
        symbols_folder_path) if isfile(join(symbols_folder_path, f))]

    for path in symbols_file_paths:
        target_folder = raw_data_folder_path + path[:-4] + '/'
        symbols = pd.read_csv(symbols_folder_path + path)

        # Make a folder
        try:
            os.mkdir(target_folder)
            print("Create a folder: " + target_folder)
        except FileExistsError:
            print("{folder} exists ".format(folder=target_folder))
        except OSError:
            print(OSError)

        for symbol in symbols.loc[:, 'symbol']:
            # Download file to that folder
            download_file(
                make_url_stock_ai(symbol, data_start_date,
                                  data_end_date, r_key),
                target_folder + symbol + ".csv")
