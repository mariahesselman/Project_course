"""Cross validation"""
import parser_i
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score

   
def crossvalidation(input_data):
	"""5-fold crossval testing different window sizes""" 
    for window in range(3,32,2):
        X, Y = parser_i.onehot(input_data, window)        
        clf = svm.SVC()
        score = cross_val_score(clf, X, Y, cv=5, verbose=True)
        score = np.average(score)
        print(window, score)                  


if __name__ == '__main__':
    crossvalidation('../datasets/dataset')
