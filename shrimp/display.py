# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 19:23:04 2016

@author: Wasit
"""
import numpy as np
import cv2
if __name__=='__main__':
    window_name='display'
    filename="coins"
    im=cv2.imread(filename +'.png')#BGR
    ol=im.copy()    
    cl=cv2.imread(filename+'predict.png',0)
    if cl is None:# not found
         cl=np.zeros( (im.shape[0],im.shape[1]),dtype=np.uint8 )
    else:
        for x in xrange(cl.shape[1]):
                for y in xrange(cl.shape[0]):
                    if cl[y,x]:
                        ol[y,x,2] = im[y,x,2]/2
    cv2.imshow(window_name, ol)