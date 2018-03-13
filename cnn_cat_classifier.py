# coding: utf-8
from os import listdir
from os.path import isfile, join

cat_dir = 'cat/'
not_cat_dir = 'not-cat/'

cat_files = [f for f in listdir(cat_dir) if isfile(join(cat_dir, f))]
not_cat_files = [f for f in listdir(not_cat_dir) if isfile(join(not_cat_dir, f))]
print(cat_files)
print(not_cat_files)

"""
import time
import numpy as np
import h5py
import matplotlib.pyplot as plt
import scipy
from PIL import Image
from scipy import ndimage
from dnn_app_utils_v2 import *

get_ipython().magic('matplotlib inline')
plt.rcParams['figure.figsize'] = (5.0, 4.0) # set default size of plots
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'

get_ipython().magic('load_ext autoreload')
get_ipython().magic('autoreload 2')

np.random.seed(1)


# ## 2 - Dataset
# 
# You will use the same "Cat vs non-Cat" dataset as in "Logistic Regression as a Neural Network" (Assignment 2). The model you had built had 70% test accuracy on classifying cats vs non-cats images. Hopefully, your new model will perform a better!
# 
# **Problem Statement**: You are given a dataset ("data.h5") containing:
#     - a training set of m_train images labelled as cat (1) or non-cat (0)
#     - a test set of m_test images labelled as cat and non-cat
#     - each image is of shape (num_px, num_px, 3) where 3 is for the 3 channels (RGB).
# 
# Let's get more familiar with the dataset. Load the data by running the cell below.

# In[2]:

train_x_orig, train_y, test_x_orig, test_y, classes = load_data()
"""

