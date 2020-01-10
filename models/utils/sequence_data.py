import numpy as np


def data_to_sequences_and_labels(data, lookback, step, min_idx, max_idx, delay, label_index):
    if max_idx is None:
        max_idx = len(data)-delay-1
    i = min_idx + lookback - 1
    rows = range(i, max_idx+1)

    return (data_to_sequences(data, lookback, step, rows),
            data_to_labels(data, delay, rows, label_index))


def data_to_labels(data, delay, rows, label_index):
    labels = np.zeros((len(rows), ))
    for j, row in enumerate(rows):
        labels[j] = 1 if 1 in data[row +
                                   1:(row + delay + 1), label_index] else 0
    return labels


def data_to_sequences(data, lookback, step, rows):
    samples = np.zeros((len(rows), lookback // step, (data.shape[-1])))

    for j, row in enumerate(rows):
        indices = range(row - lookback + 1, row + 1, step)
        samples[j] = data[indices]
    return samples
