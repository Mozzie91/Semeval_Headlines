from __future__ import print_function
import numpy as np
np.random.seed(1337)  # for reproducibility

import keras
import matplotlib.pyplot as plt


class LossHistory(keras.callbacks.Callback):
    def on_train_begin(self, logs={}):
        self.losses = {'batch': [], 'epoch': []}
        self.cosine_metric = {'batch': [], 'epoch': []}
        self.val_loss = {'batch': [], 'epoch': []}
        self.val_cosine_metric = {'batch': [], 'epoch': []}

    def on_batch_end(self, batch, logs={}):
        self.losses['batch'].append(logs.get('loss'))
        self.cosine_metric['batch'].append(logs.get('cosine_metric'))
        self.val_loss['batch'].append(logs.get('val_loss'))
        self.val_cosine_metric['batch'].append((logs.get('val_cosine_metric')))

    def on_epoch_end(self, batch, logs={}):
        self.losses['epoch'].append(logs.get('loss'))
        self.cosine_metric['epoch'].append(logs.get('cosine_metric'))
        self.val_loss['epoch'].append(logs.get('val_loss'))
        self.val_cosine_metric['epoch'].append((logs.get('val_cosine_metric')))

    def loss_plot(self, loss_type):
        iters = range(len(self.losses[loss_type]))
        plt.figure()
        # acc
        #plt.plot(iters, self.cosine_metric[loss_type], 'r', label='train cosine_proximity')
        # loss
        plt.plot(iters, self.losses[loss_type], 'g', label='train loss')
        if loss_type == 'epoch':
            # val_acc
            #plt.plot(iters, self.val_cosine_metric[loss_type], 'b', label='val cosine_proximity')
            # val_loss
            plt.plot(iters, self.val_loss[loss_type], 'k', label='val loss')
        plt.grid(True)
        plt.xlabel(loss_type)
        plt.ylabel('acc-loss')
        #plt.legend(loc="lower right")
        plt.legend(loc="upper right")
        plt.show()




