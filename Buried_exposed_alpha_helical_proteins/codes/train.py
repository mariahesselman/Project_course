from sklearn.externals import joblib
import numpy as np
from sklearn import svm
#This function takes my SVM_input file generated in parser_i.py and fits an SVM model. I save my model as model.sav
def train(input_data):    
    input_vector = np.load(input_data)    
    X = input_vector['x']
    Y = input_vector['y']
    
    clf = svm.SVC()
    clf.fit(X, Y)
    
    filename = 'model.sav'
    joblib.dump(clf, filename)
if __name__ == '__main__':
    train('SVM_input.npz')
