# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 00:25:57 2016

@author: Wasit
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn.datasets import load_iris

def generate_rf(X_train, y_train, X_test, y_test):
    rf = RandomForestClassifier(n_estimators=5, min_samples_leaf=3)
    rf.fit(X_train, y_train)
    print "rf score ", rf.score(X_test, y_test)
    return rf

def combine_rfs(rf_a, rf_b):
    rf_a.estimators_ += rf_b.estimators_
    rf_a.n_estimators = len(rf_a.estimators_)
    return rf_a

iris = load_iris()
X, y = iris.data[:, [0,1,2]], iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.33)
# in the line below, we create 10 random forest classifier models
rfs = [generate_rf(X_train, y_train, X_test, y_test) for i in xrange(10)]
# in this step below, we combine the list of random forest models into one giant model
rf_combined = reduce(combine_rfs, rfs)
# the combined model scores better than *most* of the component models
print "rf combined score", rf_combined.score(X_test, y_test)