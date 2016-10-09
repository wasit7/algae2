import numpy as np
import pickle
import os
from sklearn.cross_validation import cross_val_score
from sklearn.ensemble import ExtraTreesClassifier
from datetime import datetime
dataset_path="dataset"
with open(os.path.join(dataset_path,'xy.pic'),'rb') as f:
    xy = pickle.load(f)
x= xy['x']
y= xy['y']

clf_et = ExtraTreesClassifier(n_estimators=4, max_depth=None, n_jobs=-1,
    min_samples_split=1, random_state=datetime.now().second, 
    max_features=None, verbose=True)
#scores = cross_val_score(clf_et, x, y, cv=5)
#print scores
#print "--Extra Tree: %s"%scores.mean()
print "--Training"
t=clf_et.fit( x, y)
fname=datetime.now().strftime("%m%d%H%M%S")+'.tree'
with open(os.path.join(dataset_path,fname),'wb') as f:
    pickle.dump(t,f, pickle.HIGHEST_PROTOCOL)

print '--Finished'