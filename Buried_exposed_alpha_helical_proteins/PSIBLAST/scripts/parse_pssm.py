import sys 
sys.path.insert(0,"../../codes")
import parser_i
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
import pickle

def parse_pssm(dataset, window):
    names = parser_i.parse_name(dataset)
    seq = parser_i.parse_seq(dataset)
    top = parser_i.parse_topo(dataset)

    #print(names, seq, top)
    X_train, X_test, Y_train, Y_test = train_test_split(names, top, test_size=0.3, random_state=0)
    
    pssm_list = []
    
    for name in X_train:
        pssm = '../pssm/' + name + '.fasta.pssm'
        pssm_list.append(np.genfromtxt(pssm, skip_header=3, skip_footer=5, usecols=range(22,42)))
        
    X_train = pssm_list
    
    X_train_changed, array_numbering = extract_pssms(X_train, window)
    
    burial = {'E':1, 'B':-1}
    Y_train_changed = []
    for proteins in Y_train:    
        for topologies in proteins:
            y = burial[topologies]
            Y_train_changed.append(y)
    #print(Y_train_changed)
    clf = svm.SVC()
    clf.fit(X_train_changed, Y_train_changed)
    filename = 'pssm_model.sav'
    pickle.dump(clf, open(filename, 'wb'))
    
    

def extract_pssms(pssm_list, window):
    padding = window // 2
    arrays = []
    numbering = []
    
    for number, matrix in enumerate(pssm_list):
        length = len(matrix)
        training = np.zeros((length, window, 20))
        decimal_pssm = matrix / 100
        pad_matrix = np.vstack([np.zeros((padding, 20)), decimal_pssm, np.zeros((padding, 20))])
        for aa in range(length):
            training[aa] = pad_matrix[aa:aa + window]
            numbering.append(number)
        arrays.append(training.reshape(length, window *20))
    return np.vstack(arrays), numbering
            
           
if __name__ == '__main__':  
    parse_pssm('../../codes/dataset', 3)
