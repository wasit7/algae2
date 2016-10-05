# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 00:54:26 2016

@author: Wasit
"""
from  algae_prep import dataset_path
import pickle 
import os, fnmatch

def combine_trees(et_a, et_b):
    et_a.estimators_ += et_b.estimators_
    et_a.n_estimators = len(et_a.estimators_)
    return et_a

t_list=fnmatch.filter(os.listdir(dataset_path), '*.tree')
tree_list=[]
for i in t_list:
    with open(os.path.join(dataset_path, i ),'rb') as f:
        tree_list.append(pickle.load(f))
forest = reduce(combine_trees, tree_list)
with open(os.path.join(dataset_path,'forest.pic'),'wb') as f:
    pickle.dump(forest,f, pickle.HIGHEST_PROTOCOL)