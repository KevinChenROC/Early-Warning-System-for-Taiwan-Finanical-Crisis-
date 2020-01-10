import os
import shutil

from data_transform.transform_raw_data import get_transformed_data
from data_fetching.data_downloader import download_raw_data
from data_transform.util.store_data import store_dataframe
from config import *
from data_transform.util.file_extension import remove_extension

raw_dataset_paths = [STOCK_INDX_PATH, FOREX_PATH] + [BOND_INDX_PATH,
                                                     MACRO_INDTRS_PATH, BISR_PATH]

# value columns for selecting close prices for each category of data
val_columns = ['Close']*2 + ['Value'] * 3

if not os.path.isfile(LATEST_DATA_FOR_MODEL_PATH):
    print("Preparing to create new " +
          LATEST_DATA_FOR_MODEL_PATH)
    # remove folder recursively
    print("Remove all raw data...")
    folder_list = [f for f in os.listdir(RAW_DATA_PATH)]
    for f in folder_list:
        shutil.rmtree(RAW_DATA_PATH+f)

print("\n" + "="*15 + "Download raw data." + "="*15 + "\n")
download_raw_data(SYMBOLS_PATH, RAW_DATA_PATH,
                  START_DATE, END_DATE, R_KEY)

print("\n" + "="*15 + "Transform and store raw data" + "=" * 15 + "\n")
df_transformed = get_transformed_data(
    raw_dataset_paths, val_columns, RAW_DATA_PATH, START_DATE, END_DATE, RETURN_DISTR_WINDOW, MARKET_CRASH_THRESHOLD)

assert((len(df_transformed[df_transformed.Crisis == 1]) +
        len(df_transformed[df_transformed.Crisis == 0])) == len(df_transformed))

# store this DF
store_dataframe(df_transformed, 'csv', LATEST_DATA_FOR_MODEL_PATH)

print("ETL finished")
