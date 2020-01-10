import numpy as np


def probs_to_binary_classes(preds, threshold=0.5):
    """
    preds: np array
    threshold: scalar
    """
    return np.where(preds > threshold, 1, 0)


def min_avg_model_loss(history):
    """return the epoch and its min avg loss"""
    loss = np.array(history.history['loss'])
    val_loss = np.array(history.history['val_loss'])
    avg_loss = list((loss + val_loss)/2)
    min_idx = avg_loss.index(min(avg_loss))

    return (min_idx+1), avg_loss[min_idx]
