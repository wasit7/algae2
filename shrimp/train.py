import numpy as np
import cv2
import pickle
from sklearn.cross_validation import cross_val_score
from sklearn.ensemble import ExtraTreesClassifier
filename="dataset"
im=cv2.imread(filename +'.png')#BGR
#window_name='shrimp'
#height, width, depth = im.shape
#im=cv2.resize(im, (width/2, height/2),interpolation = cv2.INTER_CUBIC)


cl=cv2.imread(filename+'_label.png',0)#BGR - Gray Scale
#cl=cv2.resize(cl, (im.shape[0], im.shape[1]),interpolation = cv2.INTER_CUBIC)

imshape=im.shape[0]*im.shape[1]
im=np.reshape(im,(imshape,3))
clshape=cl.shape[0]*cl.shape[1]
cl=np.reshape(cl,(clshape))

#x=np.random.permutation(im)
clf_et = ExtraTreesClassifier(n_estimators=10, max_depth=None, 
    min_samples_split=1, random_state=None, max_features=None)
scores = cross_val_score(clf_et, im, cl, cv=5)
print scores
print "--Extra Tree: %s"%scores.mean()
forest=clf_et.fit(im, cl)
with open('forest.pic','wb') as f:
    pickle.dump(forest,f, pickle.HIGHEST_PROTOCOL)

print '--finished'