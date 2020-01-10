import os

import pandas as pd
from pandas.util.testing import assert_frame_equal

from ..util.store_data import store_dataframe


def run_tests():
    df = pd.read_csv("datasets/raw_data/stock_indexes/^TWII.csv",
                     header=0, parse_dates=[0], index_col=0)
    test_path = "./test_data.csv"

    # store df and read the stored df for testing
    store_dataframe(df, 'csv', test_path)
    test_df = pd.read_csv(test_path, header=0, parse_dates=[0], index_col=0)

    assert_frame_equal(df, test_df)
    assert df.shape == df.shape

    # delete the test df file
    if os.path.exists(test_path):
        os.remove(test_path)
    else:
        print("{path} does not exist".format(path=test_path))


run_tests()
