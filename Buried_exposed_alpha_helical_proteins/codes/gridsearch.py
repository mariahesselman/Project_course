"""Testing different parameters"""
import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.svm import LinearSVC
from sklearn.externals import joblib
from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

def optimize_params(input_file): 
    """testing different kernels, c values and gamma values"""
    filz = np.load(input_file)    
    x = filz['x']
    y = filz['y']    
    #x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.30)    
    svc = svm.SVC()
    parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10], 'gamma':[0.01, 0.05, 0.1]}
    clf = GridSearchCV(svc, parameters)
    clf.fit(x, y)
    res = pd.DataFrame(clf.cv_results_)
    res.to_csv('../result_files/optimize_c.csv', sep='\t', encoding='UTF-8')
   
if __name__ == '__main__':
    optimize_params('SVM_input.npz')
