# coding: utf-8
# Move functions from 'dnn cat classifier.ipynb'

import math
import numpy as np

def random_mini_batches(X, Y, mini_batch_size = 64, seed = 0):
    """
    Arguments:
        X -- input data, of shape (input size, number of examples) (m, Hi, Wi, Ci)
        Y -- true "label" vector, of shape (1, number of examples) (m, n_y)
        mini_batch_size -- size of the mini-batches, integer
        
    Returns:
        mini_batches -- list of synchronous (mini_batch_X, mini_batch_Y)
    """
    
    np.random.seed(seed)
    m = X.shape[0]
    mini_batches = []
    
    permutation = list(np.random.permutation(m))
    shuffled_X = X[permutation,:,:,:]
    shuffled_Y = Y[permutation,:]
    
    num_complete_minibatches = math.floor(m/mini_batch_size)
    for k in range(0, num_complete_minibatches):
        mini_batch_X = shuffled_X[k*mini_batch_size:(k+1)*mini_batch_size,:,:,:]
        mini_batch_Y = shuffled_Y[k*mini_batch_size:(k+1)*mini_batch_size,:]
        mini_batch = (mini_batch_X, mini_batch_Y)
        mini_batches.append(mini_batch)
        
    if m % mini_batch_size != 0:
        mini_batch_X = shuffled_X[num_complete_minibatches*mini_batch_size:m,:,:,:]
        mini_batch_Y = shuffled_Y[num_complete_minibatches*mini_batch_size:m,:]
        mini_batch = (mini_batch_X, mini_batch_Y)
        mini_batches.append(mini_batch)
        
    return mini_batches