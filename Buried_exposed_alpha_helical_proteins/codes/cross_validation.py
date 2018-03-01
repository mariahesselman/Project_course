import parser_i
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
#This function takes my dataset and runs a 3-fold cross validation with window sizes from 3 to 31 with steps of 2. It prints an average of the score of each window size.   
def crossvalidation(input_data): 
    for window in range(3,32,2):
        X, Y = parser_i.onehot(input_data, window)        
        clf = svm.SVC()
        score = cross_val_score(clf, X, Y, cv=3, verbose=True)
        score = np.average(score)
        print(window, score)                  
if __name__ == '__main__':
    crossvalidation('dataset')
