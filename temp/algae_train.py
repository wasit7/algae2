import numpy as np
import pickle
import os
from sklearn.cross_validation import cross_val_score
from sklearn.ensemble import ExtraTreesClassifier
dataset_path="dataset"
with open(os.path.join(dataset_path,'xy.pic'),'rb') as f:
    xy = pickle.load(f)
x= xy['x']
y= xy['y']

clf_et = ExtraTreesClassifier(n_estimators=10, max_depth=20, 
    min_samples_split=5, random_state=None, max_features=None, verbose=True)
#scores = cross_val_score(clf_et, x, y, cv=5)
#print scores
#print "--Extra Tree: %s"%scores.mean()
print "--Training"
forest=clf_et.fit( x, y)
with open(os.path.join(dataset_path,'forest.pic'),'wb') as f:
    pickle.dump(forest,f, pickle.HIGHEST_PROTOCOL)

print '--Finished'