import parser_i
from sklearn.externals import joblib
import numpy as np

loaded_model = joblib.load('model.sav')
aa = '0GALMFWKQESPVICYHRNDT'
AA_TO_INT = dict((c, i) for i, c in enumerate(aa))

def parse_fasta(filename):
    input_file = open(filename, 'r')
    id_list = []
    seq_list = []    
    for line in input_file:
        if line.startswith('>'):
            id_list.append(line.strip())
        else:
            seq_list.append(line.strip())
    print(id_list)
    print(seq_list)
    return seq_list


def windowmaking(seq, window):
    padding = window//2
    window_list = []    
    for sequence in seq:
        sequence = ((padding*'0') + sequence + (padding*'0'))
        for residue in range(0, len(sequence)):
            if residue+(window) > len(sequence):
                break
            window_list.append(sequence[residue:residue+window])
        return window_list


def window_int(windows): 
    windows_in_integers = []
    for window in windows:
        windows_in_int = [AA_TO_INT[aa] for aa in window]    
        windows_in_integers.append(windows_in_int)
    return windows_in_integers    


def onehot(int_wind): 
    onehot_encoded_windows = []
    for window in int_wind:
        this_window = []
        for residue in window:
            letter = [0 for _ in range(len(aa))]
            if residue != 0:      
                letter[residue] = 1
            else:
                pass
            this_window.extend(letter)           
        onehot_encoded_windows.append(this_window)
    return onehot_encoded_windows    


def predict(sequence_in_windows, seqsy):
    result = loaded_model.predict(sequence_in_windows)
    results = result
    burial_decode = {1:'E', -1:'B'}
    decoded_results = []
    for element in results:
        decoded_results.append(burial_decode[element])
    print(results)
    print(seqsy, decoded_results)
    return decoded_results    
if __name__ == '__main__':
    seqsy = parse_fasta('fastatest.fasta')
    windowz = windowmaking(seqsy, 25)
    int_wind = window_int(windowz)
    sequence_in_windows = onehot(int_wind)
    predict(sequence_in_windows, seqsy)
    
