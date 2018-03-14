"""Predicts topology from a position specific frequency table"""
import pickle
import sys
import numpy as np


LOADED_MODEL = pickle.load(open('../scripts/pssm_model.sav', 'rb'))


def predict(pssm_file):
    """Takes a PSSM file and predicts the topology"""
    window = 3
    padding = window // 2
    pssm = np.genfromtxt(pssm_file, skip_header=3, skip_footer=5, usecols=range(22, 42))
    length = len(pssm)
    predicting_array = np.zeros((length, window, 20))
    decimal_pssm = pssm / 100
    pad_matrix = np.vstack([np.zeros((padding, 20)), decimal_pssm, np.zeros((padding, 20))])
    arrays = []

    for aa in range(length):
        predicting_array[aa] = pad_matrix[aa:aa + window]
    arrays.append(predicting_array.reshape(length, window *20))
    arrays = np.vstack(arrays)
    results = LOADED_MODEL.predict(arrays)
    burial_decode = {1:'E', -1:'B'}
    results_decode = []

    for topology in results:
        results_decode.append(burial_decode[topology])
    string_result = ''.join(results_decode)

    with open('../pssm_svm_predictions.txt', 'a') as f:
        f.write(pssm_file[:-11] + '\n')
        f.write(string_result + '\n')
        f.close()
    print(pssm_file[:-11])
    print(string_result)


if __name__ == '__main__':
    #PSSM_FILE = sys.argv[1]
    #predict(PSSM_FILE)
    predict('../pssm/>d1du0b_.a.4.1.1.fasta.pssm')
