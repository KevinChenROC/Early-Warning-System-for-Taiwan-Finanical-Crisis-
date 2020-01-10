from .preprocessing import min_avg_model_loss


def hyperparams_search(model_func, input_shape, is_verbose, train_X, train_Y, val_X, val_Y, num_epoch, hidden_units, n_layers, l2_weights):
    """return the best combination of params with minimal average of train and val loss"""
    min_avg_loss = 999999
    best_params = {}
    for l2_weight in l2_weights:
        for n_layer in n_layers:
            for hidden_unit in hidden_units:
                # compile
                model = model_func(hidden_unit, n_layer,
                                   l2_weight, input_shape)

                # fit the model
                history = model.fit(train_X, train_Y,
                                    validation_data=(val_X, val_Y),
                                    epochs=num_epoch,
                                    verbose=is_verbose)
                cur_num_epoch, cur_avg_loss = min_avg_model_loss(history)

                cur_params = {}
                cur_params['epochs'] = cur_num_epoch
                cur_params['n_layer'] = n_layer
                cur_params['hidden_unti'] = hidden_unit
                cur_params['l2_weight'] = l2_weight

                print("cur_avg_loss = {0}, cur_params = {1}".format(
                    cur_avg_loss, cur_params))

                if(cur_avg_loss < min_avg_loss):
                    min_avg_loss = cur_avg_loss
                    best_params = cur_params

    return best_params
