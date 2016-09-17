# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 19:12:02 2016

@author: Wasit
"""
#from sklearn.ensemble import ExtraTreesClassifier
import pickle
import cv2
import numpy as np
from  algae_prep import get_xy,dataset_path,rmax,cmax,show_overlay,hws
import os
from algae_core import cmap

with open(os.path.join(dataset_path,'train_pairs.obj'),'rb') as f:
    train_pairs = pickle.load(f)
#i=train_pairs[1]
for i in train_pairs:

    x,y=get_xy( [i] )
    oim=cv2.imread(i['raw'])#BGR
    im=cv2.resize(oim, (cmax,rmax),interpolation = cv2.INTER_CUBIC) 
    
    with open('forest.pic','rb') as f:
        forest = pickle.load(f)
    cl_p=forest.predict( x )

    cl_p.resize((rmax-2*hws,cmax-2*hws))
    #cv2.imwrite(os.path.join(dataset_path,'_predict.png'),cl_p)
    
    ol=im.copy()
    for r in xrange(rmax-2*hws):
        for c in xrange(cmax-2*hws):
            if cl_p[r,c]==1:
                ol[r+hws,c+hws] = cmap[0]
    cv2.imshow('predict', ol)
    
    from skimage import measure
    blobs_labels,num = measure.label(cl_p, background=0,return_num=True,connectivity=2)
    print 'totol object is %d'%num
    cv2.imshow('count',blobs_labels*255)
    if cv2.waitKey(0) == ord(' '):
        pass