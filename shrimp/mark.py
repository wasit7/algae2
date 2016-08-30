# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 10:21:22 2016

@author: Wasit
"""
import numpy as np
import cv2

def callback(event,x,y,flags,param):
    #print "event: %s"%event
    #print "(x, y), (flag param): (%d %d) (%d %s)"% (x, y,flags,param)
    #print cl.shape
    if event==cv2.EVENT_MOUSEMOVE and cv2.EVENT_FLAG_LBUTTON:
        if cl[y,x]==0:
            r=5
            for i in xrange(-r,r):
                for j in xrange(-r,r):
                    if np.sqrt( i**2 + j**2 )<r: 
                        cl[y+j,x+i]=1
                        ol[y+j,x+i,2] = im[y+j,x+i,2]/16
        else:
            r=10
            for i in xrange(-r,r):
                for j in xrange(-r,r):
                    if np.sqrt( i**2 + j**2 )<r: 
                        cl[y+j,x+i]=0
                        ol[y+j,x+i,2] = im[y+j,x+i,2]
        cv2.imshow(window_name,ol)
        #cv2.imshow('class',cl)
    if event==cv2.EVENT_RBUTTONDOWN:
        f=filename+'_label'+'.png'
        cv2.imwrite(f,cl)
        print '--saved to %s'%f
if __name__=='__main__':
    filename="dataset"
    im=cv2.imread(filename +'.png')#BGR
    window_name=filename
    #height, width, depth = im.shape
    #im=cv2.resize(im, (width/2, height/2),interpolation = cv2.INTER_CUBIC)
    ol=im.copy()    
    cl=cv2.imread(filename+'_label.png',0)
    #print cl.shape
    if cl is None:# not found
         cl=np.zeros( (im.shape[0],im.shape[1]),dtype=np.uint8 )
    else:
        for x in xrange(cl.shape[1]):
                for y in xrange(cl.shape[0]):
                    if cl[y,x]:
                        ol[y,x,2] = im[y,x,2]/16
    cv2.imshow(window_name, ol)
    #cv2.imshow('class',255*cl)
    cv2.setMouseCallback(window_name,callback)