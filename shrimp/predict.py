# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 19:12:02 2016

@author: Wasit
"""
#from sklearn.ensemble import ExtraTreesClassifier
import pickle
import cv2
import numpy as np

filename="dataset"
im=cv2.imread(filename +'.png')#BGR
cl_p=np.zeros( (im.shape[0],im.shape[1]),dtype=np.uint8 )
rmax=im.shape[0]
cmax=im.shape[1]
n=rmax * cmax
im_p=np.reshape(im,(n,3))
cl_p=np.reshape(cl_p,(n))

with open('forest.pic','rb') as f:
    forest = pickle.load(f)
cl_p=forest.predict( im_p )
cl_p.resize((rmax,cmax))
cv2.imwrite(filename+'_predict.png',cl_p)

ol=im.copy()
for x in xrange(cl_p.shape[1]):
    for y in xrange(cl_p.shape[0]):
        if cl_p[y,x]:
            ol[y,x,2] = im[y,x,2]/16
cv2.imshow('predict', ol)

from skimage import measure
blobs_labels,num = measure.label(cl_p, background=0,return_num=True,connectivity=2)
print 'totol object is %d'%num
cv2.imshow('count',blobs_labels*255)