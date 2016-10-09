# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 19:12:02 2016

@author: Wasit
"""
#from sklearn.ensemble import ExtraTreesClassifier
import pickle
import cv2

from  algae_prep import get_xy,dataset_path,rmax,cmax,hws
from algae_core import cmap
import os, fnmatch
from skimage import measure, filters
from skimage.filters import threshold_otsu
    
raw_files=fnmatch.filter(os.listdir(dataset_path), '*.jpg')
raw_list=[i[:-4] for i in raw_files]

label_files=fnmatch.filter(os.listdir(dataset_path), '*.png')
label_list={i[:-4]:None for i in label_files}

predict_list=[]
for count,i in enumerate(raw_list):
    if i not in label_list:
         predict_list.append({
             'raw': os.path.join(dataset_path,i)+'.jpg',
            'label': '.png',
            })

for i in predict_list:
    x,y=get_xy( [i] )
    oim=cv2.imread(i['raw'])#BGR
    im=cv2.resize(oim, (cmax,rmax),interpolation = cv2.INTER_CUBIC) 
    
    with open(os.path.join(dataset_path,'forest.pic'),'rb') as f:
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
    

    a=filters.gaussian_filter(cl_p.astype(float), sigma=1.5)
    thresh = threshold_otsu(a)
    binary = a > thresh
    blobs_labels,num = measure.label(binary, background=0,return_num=True,connectivity=2)
    print 'totol object is %d'%num
    cv2.imshow('count',blobs_labels*1024)
    print "Press space to predict next image"
    if cv2.waitKey(0) == ord(' '):
        pass