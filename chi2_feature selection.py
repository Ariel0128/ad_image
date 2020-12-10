# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 10:18:23 2018

@author: rpear
"""
import pandas as pd
import numpy
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score


rawdata = pd.read_csv('cleaned.csv')
array = rawdata.values
X = array[:, 0:1558]
Y = array[:, 1558]
fs1 = SelectKBest(chi2, k=900)
application = fs1.fit(X, Y)
numpy.set_printoptions(precision=3)
print(application.scores_)
result = application.transform(

X_train, X_test, Y_train, Y_test = train_test_split(fs1_d, Y, random_state=1, train_size=0.64)  # split

sm1 = SMOTE(random_state=10, k_neighbors=3, sampling_strategy=0.33)X)
f_number = fs1.get_support(indices=True)
# print(f_number)
fs1_d = rawdata.iloc[:, f_number]
# last = fs1_d.insert(900, 'class', Y) # to combine the selected feature and the class value
# configure the SMOTE 0.33 = desired ratio of minority over majority

X_sm1, Y_sm1 = sm1.fit_resample(X_train, Y_train)

clf = DecisionTreeClassifier(criterion="entropy", min_samples_split=2)
# entropy means the information gain; another default criterion is "gini" for the gini impurity
# min_sample_split corresponds to min num Object in WEKA - online pruning
clf = clf.fit(X_sm1, Y_sm1)
clf_pred = clf.predict(X_test)
print(accuracy_score(Y_test, clf_pred))

from sklearn.metrics import roc_curve, auc

false_positive_rate, true_positive_rate, thresholds = roc_curve(Y_test, clf_pred, pos_label='ad.')
roc_auc = auc(false_positive_rate, true_positive_rate)
print(roc_auc)

X_test.iloc()



