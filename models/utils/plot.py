import matplotlib.pyplot as plt


def plot_train_validation_metric(history, train_metric, val_metric):
    val_acc = history.history[val_metric]
    acc = history.history[train_metric]
    epochs = range(1, len(acc)+1)

    plt.figure(figsize=(15, 6), dpi=70)

    plt.plot(epochs, acc, 'r', label=train_metric)
    plt.plot(epochs, val_acc, 'b', label=val_metric)
    plt.title("Training and validation metrics")
    plt.legend()

    plt.show()
