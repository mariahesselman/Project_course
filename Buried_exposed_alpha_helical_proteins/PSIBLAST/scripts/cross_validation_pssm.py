"""Cross validation"""
import parse_pssm
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score

   
def crossvalidation(names, top):
    """5-fold crossval testing different window sizes""" 
    for window in range(7,16,2):
        X, Y = parse_pssm.extract_pssms(names, top, window)        
        clf = svm.SVC()
        score = cross_val_score(clf, X, Y, cv=5, verbose=True)
        score = np.average(score)
        print(window, score)                  


if __name__ == '__main__':
    NAMES, SEQ, TOP = parse_pssm.extract_info('../../datasets/dataset')
    crossvalidation(NAMES, TOP)
