# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 10:21:22 2016

@author: Wasit
"""
import numpy as np
import cv2
import os
cmax=800
rmax=600
dataset_path=os.path.join('dataset')

cmap=np.array([  
        ( 0  , 255, 255,  ),
        ( 64 , 177, 255,  ),
        ( 94 , 210, 94 ,  ),
        ( 40 , 39 , 214,  ),
        ( 150  , 0  , 255,  ),
        ( 0  , 255, 0  ,  ),
        ( 194, 119, 227,  ),
        ( 255, 0  , 0  ,  ),
        ( 34 , 189, 188,  ),
        ( 207, 190, 23 ,  ),])
def callback(event,x,y,flags,param):
    #print "event: %s"%event
    #print "(x, y), (flag param): (%d %d) (%d %s)"% (x, y,flags,param)
    #print cl.shape
    if flags==cv2.EVENT_FLAG_LBUTTON + cv2.EVENT_FLAG_CTRLKEY:
        r=8
        for i in xrange(-r,r):
            for j in xrange(-r,r):
                if np.sqrt( i**2 + j**2 )<r: 
                    cl[y+j,x+i]=cc
                    ol[y+j,x+i] = cmap[cc-1]
    if flags==cv2.EVENT_FLAG_LBUTTON + cv2.EVENT_FLAG_ALTKEY:
        r=16
        for i in xrange(-r,r):
            for j in xrange(-r,r):
                if np.sqrt( i**2 + j**2 )<r: 
                    cl[y+j,x+i]=0
                    ol[y+j,x+i] = im[y+j,x+i]
    
        #cv2.imshow('class',cl)
    if event==cv2.EVENT_LBUTTONDOWN:
        r=8
        for i in xrange(-r,r):
            for j in xrange(-r,r):
                if np.sqrt( i**2 + j**2 )<r: 
                    cl[y+j,x+i]=cc
                    ol[y+j,x+i] = cmap[cc-1]
    cv2.imshow(window_name,ol)
    
def reload(flist,index):
    oim=cv2.imread(flist[index])#BGR
    
    #height, width, depth = im.shape
    #im=cv2.resize(im, (width/2, height/2),interpolation = cv2.INTER_CUBIC)
    im=cv2.resize(oim, (cmax,rmax),interpolation = cv2.INTER_CUBIC)    
    ol=im.copy()    
    ocl=cv2.imread(flist[index][:-3]+'png',0)
    
    #print cl.shape
    if ocl is None:# not found
         cl=np.zeros( (im.shape[0],im.shape[1]),dtype=np.uint8 )
    else:
        cl=cv2.resize(ocl, (cmax,rmax),interpolation = cv2.INTER_NEAREST )
        for x in xrange(cl.shape[1]):
                for y in xrange(cl.shape[0]):
                    if cl[y,x]:
                        ol[y,x] = cmap[cl[y,x]-1]
    return flist[index],im,cl,ol
if __name__=='__main__':
    import os, fnmatch
    fname=fnmatch.filter(os.listdir(dataset_path), '*.jpg')
    flist=[os.path.join(dataset_path,i) for i in fname]
    index=0

    filename,im,cl,ol=reload(flist, index)
    window_name="algae_marker"    
    cv2.imshow(window_name, ol)
    #cv2.imshow('class',255*cl)
    cv2.setMouseCallback(window_name,callback)
    #Upkey : 2490368
    #DownKey : 2621440
    #LeftKey : 2424832
    #RightKey: 2555904
    key=''
    cc=1
    while key!= 27:
        key=cv2.waitKey(25)
        if key==48:
            cc=10
            print "class: %d"%cc
        elif 48<key<=57:
            cc=key-48
            print "class: %d"%cc            
        elif key == 2424832:
            index=(index+len(flist)-1)%len(flist)
            filename,im,cl,ol=reload(flist, index)
            cv2.imshow(window_name, ol)
            print filename
        elif key ==2555904:
            index=(index+len(flist)+1)%len(flist)
            filename,im,cl,ol=reload(flist, index)
            cv2.imshow(window_name, ol)
            print filename
        elif key == ord(' '):
            f=filename[:-3]+'png'
            cv2.imwrite(f,cl)
            print '--saved to %s'%f
    cv2.destroyAllWindows() 