import parser_i
import numpy as np
from sklearn import svm
from sklearn.externals import joblib
from sklearn.model_selection import cross_val_score
  
def train(input_data): 
    for window in range(3,32,2):
        X, Y = parser_i.onehot('dataset', window)
    #input_vector = np.load(input_data)    
    #X = input_vector['x']
    #Y = input_vector['y']
    
        clf = svm.SVC()
        score = cross_val_score(clf, X, Y, cv=3, verbose=True)
        score = np.average(score)
    #clf.fit(X, Y)
        print(window, score)
       
   
    '''
    result = clf.predict(X)
    results = list(result)
    burial_decode = {1:'E', -1:'B'}
    decoded_results = []
    for element in results:
        decoded_results.append(burial_decode[element])
    print(results)
    print(decoded_results)
    #joblib.dump(clf, input_data+'.model.pkl')
    '''
    
if __name__ == '__main__':
    train('SVM_input.npz')
