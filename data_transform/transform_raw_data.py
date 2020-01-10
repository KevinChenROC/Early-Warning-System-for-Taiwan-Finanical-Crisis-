import pandas as pd
from data_transform.util.calc_rate import calc_simple_rates
from data_transform.util.crisis_label import get_crisis_label
from data_transform.util.merge_data import merge_datasets


def get_transformed_data(dataset_paths, val_columns, raw_data_path, start_date, end_date, return_distr_window, market_crash_threshold):
    # Merge all datasets in raw folders into one
    dataset_df = merge_datasets(
        dataset_paths, val_columns, start_date, end_date)

    # Get crisis labels for each day
    tw_stock = pd.read_csv("datasets/raw_data/stock_indexes/^TWII.csv",
                           header=0, parse_dates=[0], index_col=0)
    crisis_df = get_crisis_label(
        calc_simple_rates(tw_stock['Close']).dropna(), return_distr_window, market_crash_threshold)

    # normalize all columns in
    normalized_df = (dataset_df-dataset_df.min()) / \
        (dataset_df.max()-dataset_df.min())

    # merge above dataframes into final dataset
    return normalized_df.join(crisis_df, how='inner')
