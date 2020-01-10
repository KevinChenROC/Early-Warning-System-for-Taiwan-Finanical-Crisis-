from ..util.stats import ecdf
import numpy as np


def run_tests():
    data = np.array([3, 3, 1, 4])
    assert ecdf(data, 3) == 0.75
    assert ecdf(data, 55) == 1
    assert ecdf(data, 0) == 0
    assert ecdf(data, 1.5) == 0.25
