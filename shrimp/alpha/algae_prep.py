# -*- coding: utf-8 -*-
"""
Created on 17/09/2016

@author: Wasit
"""
import numpy as np
import cv2
from skimage.feature import local_binary_pattern
from algae_core import cmap
import pickle
import os

dataset_path='dataset'

#lbp
radius = 3
cmax=640
rmax=480
hws=3
def get_image_pair(file_pair):
    """ """
    oim=cv2.imread(file_pair['raw'])#BGR
    im=cv2.resize(oim, (cmax,rmax),interpolation = cv2.INTER_CUBIC) 
       
    ocl=cv2.imread(file_pair['label'],0)
    
    #print cl.shape
    if ocl is None:# not found
        cl=np.zeros( (im.shape[0],im.shape[1]),dtype=np.uint8 )
    else:
        cl=cv2.resize(ocl, (cmax,rmax),interpolation = cv2.INTER_NEAREST )
    
    print "raw: %s, label: %s"%(file_pair['raw'], file_pair['label'])
    
    im_grey=cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    lbp = local_binary_pattern( im_grey, 8 * radius, radius, 'uniform')
    #cv2.imshow("lbp", lbp)
    return cl,im,lbp

def show_overlay(cl,im):
    ol=im.copy() 
    for r in xrange(rmax):
        for c in xrange(cmax):
            if cl[r,c]:
                ol[r,c] = cmap[cl[r,c]-1]
    cv2.imshow("overlay", ol)

def get_xy(train_pairs):
    xrmax= ( (rmax-2*hws)*(cmax-2*hws)*len(train_pairs) )
    xcmax= 3+(2*hws)**2
    yrmax= ( (rmax-2*hws)*(cmax-2*hws)*len(train_pairs) )
    x=np.zeros((xrmax,xcmax), dtype=np.uint8)
    y=np.zeros((yrmax), dtype=np.uint8)
    k=0
    for count,i in enumerate(train_pairs):    
        print "------- processed %d from %d"%(count,len(train_pairs))
	cl,im,lbp=get_image_pair(i)
        #show_overlay(cl,im)
        if im.shape[0]!=rmax or im.shape[1]!=cmax or lbp.shape[0]!=rmax or lbp.shape[1]!=cmax:
            print "Error: image pair has missmatch size."
        for r in xrange(hws,lbp.shape[0]-hws):
            for c in xrange(hws,lbp.shape[1]-hws):
                xrow=np.concatenate([im[r,c],
                        lbp[r-hws:r+hws,c-hws:c+hws].reshape(1,-1)[0],])
                x[k,:]=xrow
                y[k]=cl[r,c]
                k+=1
    return x,y
if __name__=='__main__':
    import os, fnmatch
    raw_files=fnmatch.filter(os.listdir(dataset_path), '*.jpg')
    raw_list=[i[:-4] for i in raw_files]
    
    label_files=fnmatch.filter(os.listdir(dataset_path), '*.png')
    label_list={i[:-4]:None for i in label_files}
    
    train_pairs=[]
    for count,i in enumerate(raw_list):
	if i in label_list:
            train_pairs.append({
                'raw': os.path.join(dataset_path,i)+'.jpg',
                'label': os.path.join(dataset_path,i)+'.png',
            })
    with open(os.path.join(dataset_path,'train_pairs.obj'),'wb') as f:
        pickle.dump(train_pairs, f, pickle.HIGHEST_PROTOCOL)

    x,y = get_xy(train_pairs)

    with open(os.path.join(dataset_path,'xy.pic'),'wb') as f:
        pickle.dump({'x':x, 'y':y }, f, pickle.HIGHEST_PROTOCOL)
