# hyperparamters
BATCH_SIZE = 64

# params for generator
DELAY = 10
STEP = 1  # 1 timestep = 1 day
LOOKBACK = 15

# ratio for train/val/test split
TRAIN_RATIO = 0.7
VAL_RATIO = 0.15

# For daily prediction
LAST_N_SEQUENCE = 3

BEST_MODELS_PATH = './best_models/'
BEST_FC_MODEL_PATH = BEST_MODELS_PATH + 'fc_model.h5'
BEST_LSTM_MODEL_PATH = BEST_MODELS_PATH + 'LSTM_model.h5'
