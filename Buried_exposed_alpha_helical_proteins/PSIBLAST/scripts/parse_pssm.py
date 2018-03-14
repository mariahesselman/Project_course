"""Extracts information from my pssms and trains and saves a model"""
import sys
import pickle
import numpy as np
from sklearn import svm
sys.path.insert(0, "../../codes")
import parser_i

def extract_info(dataset):
    """Extracts names, seqs and topologies from my dataset"""
    names = parser_i.parse_name(dataset)#list of gene names generated from dataset
    seq = parser_i.parse_seq(dataset)# list of seqs generated from dataset
    top = parser_i.parse_topo(dataset)# list of topologies generated from dataset
    return names, seq, top


def train_pssm(names, top, window):
    '''Takes pssms from X_train and trains and saves model'''
    pssm_list_train = []
    for name in names:
        pssm = '../pssm/' + name + '.fasta.pssm' #location of your pssms
        pssm_list_train.append(np.genfromtxt(pssm, skip_header=3, skip_footer=5, usecols=range(22, 42)))
    X_train = pssm_list_train
    X_train_changed, array_numbering = extract_pssms(X_train, window)
    burial = {'E':1, 'B':-1}
    Y_train_changed = []
    for proteins in top:
        for topologies in proteins:
            y = burial[topologies]
            Y_train_changed.append(y)
    clf = svm.SVC()
    clf.fit(X_train_changed, Y_train_changed)
    filename = 'pssm_model.sav'
    pickle.dump(clf, open(filename, 'wb'))


def extract_pssms(pssm_list, window):
    """Formats pssms"""
    padding = window // 2
    arrays = []
    numbering = []
    for number, matrix in enumerate(pssm_list):
        length = len(matrix)
        training = np.zeros((length, window, 20))
        decimal_pssm = matrix / 100
        pad_matrix = np.vstack([np.zeros((padding, 20)), decimal_pssm, np.zeros((padding, 20))])
        for j in range(length):
            training[j] = pad_matrix[j:j + window]
            numbering.append(number)
        arrays.append(training.reshape(length, window * 20))
    return np.vstack(arrays), numbering


if __name__ == '__main__':
    NAMES, SEQ, TOP = extract_info('../../codes/dataset')
    train_pssm(NAMES, TOP, 3)#called with window size 3
