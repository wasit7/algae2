# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 15:43:58 2016

@author: Wasit
"""

## lbp

import cv2
import numpy as np


from skimage.feature import local_binary_pattern


# settings for LBP
radius = 3
n_points = 8 * radius
METHOD = 'uniform'

im=cv2.imread('dataset.png',0)
cv2.imshow('original image',im)
lbp = local_binary_pattern(im, n_points, radius, METHOD)
cv2.imshow('lbp',lbp)