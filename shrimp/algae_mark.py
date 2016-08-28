# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 10:21:22 2016

@author: Wasit
"""
import numpy as np
import cv2
dataset_path='dataset'
def callback(event,x,y,flags,param):
    #print "event: %s"%event
    #print "(x, y), (flag param): (%d %d) (%d %s)"% (x, y,flags,param)
    #print cl.shape
    if flags==cv2.EVENT_FLAG_LBUTTON + cv2.EVENT_FLAG_CTRLKEY:
        r=5
        for i in xrange(-r,r):
            for j in xrange(-r,r):
                if np.sqrt( i**2 + j**2 )<r: 
                    cl[y+j,x+i]=cc
                    ol[y+j,x+i,2] = im[y+j,x+i,2]/16
    if flags==cv2.EVENT_FLAG_LBUTTON + cv2.EVENT_FLAG_ALTKEY:
        r=10
        for i in xrange(-r,r):
            for j in xrange(-r,r):
                if np.sqrt( i**2 + j**2 )<r: 
                    cl[y+j,x+i]=0
                    ol[y+j,x+i,2] = im[y+j,x+i,2]
    
        #cv2.imshow('class',cl)
    if event==cv2.EVENT_LBUTTONDOWN:
        r=5
        for i in xrange(-r,r):
            for j in xrange(-r,r):
                if np.sqrt( i**2 + j**2 )<r: 
                    cl[y+j,x+i]=1
                    ol[y+j,x+i,2] = im[y+j,x+i,2]/16
    cv2.imshow(window_name,ol)
    
def reload(flist,index):
    oim=cv2.imread(flist[index])#BGR
    
    #height, width, depth = im.shape
    #im=cv2.resize(im, (width/2, height/2),interpolation = cv2.INTER_CUBIC)
    im=cv2.resize(oim, (1024,768),interpolation = cv2.INTER_CUBIC)    
    ol=im.copy()    
    cl=cv2.imread(flist[index][:-3]+'png',0)
    #print cl.shape
    if cl is None:# not found
         cl=np.zeros( (im.shape[0],im.shape[1]),dtype=np.uint8 )
    else:
        for x in xrange(cl.shape[1]):
                for y in xrange(cl.shape[0]):
                    if cl[y,x]:
                        ol[y,x,2] = im[y,x,2]/16
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
    while key!=ord('q'):
        key=cv2.waitKey(25)
        if key==48:
            cc=10
            print cc
        elif 48<key<=57:
            cc=key-48
            print cc            
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
        elif key == ord('s'):
            f=filename[:-3]+'png'
            cv2.imwrite(f,cl)
            print '--saved to %s'%f
    cv2.destroyAllWindows() 