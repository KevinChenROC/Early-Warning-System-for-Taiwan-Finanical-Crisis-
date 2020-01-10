import numpy as np


def ecdf(sample, t):
    return sample[sample <= t].size / sample.size
