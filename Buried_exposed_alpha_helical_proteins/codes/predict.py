import parser_i
from sklearn.externals import joblib
import numpy as np

loaded_model = joblib.load('model.sav')
aa = '0GALMFWKQESPVICYHRNDT'
AA_TO_INT = dict((c, i) for i, c in enumerate(aa))
dic = {}
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
    for i in range(len(id_list)):
        dic[(id_list[i])] = (seq_list[i], )    
    return dic


def windowmaking(seq, window):
    padding = window//2
    padded_sequences = []
    window_list = []    
    for id_, sequence in dic.items():
        sequence = sequence[0]
        padded_sequences.append((padding*'0') + sequence + (padding*'0'))
        #print(sequence)
    for padded_seq in padded_sequences:
        this_wind = []
        for residue in range(len(padded_seq)):
            if residue+(window) > len(padded_seq):
                break
            this_wind.append(padded_seq[residue:residue+window])
        window_list.append(this_wind)
    #print(padded_sequences)
    #print(window_list)
    return window_list
# window_list contains a list of sequences divided into sublists of sliding windows.

def window_int(windows): 
    windows_in_integers = []
    for sequence in windows:
        temp = []
        for window in sequence:
            windows_in_int = [AA_TO_INT[aa] for aa in window]    
            temp.append(windows_in_int)
        windows_in_integers.append(temp)
    #print(windows_in_integers)
    return windows_in_integers    


def onehot(int_wind): 
    onehot_encoded_windows = []
    for sequence in int_wind:        
        for window in sequence:
            this_window = []
            for residue in window:
                letter = [0 for _ in range(len(aa))]
                if residue != 0:      
                    letter[residue] = 1
                else:
                    pass
                this_window.append(letter)           
            onehot_encoded_windows.append(this_window)
    print(len(onehot_encoded_windows))
    return onehot_encoded_windows    


def predict(sequence_in_windows, seqsy):
    for sequence in sequence_in_windows:
        result = loaded_model.predict(sequence)
        #print(result)
        burial_decode = {1:'E', -1:'B'}
        decoded_results = []
        for element in result:
            decoded_results.append(burial_decode[element])
    #print(results)
    #print(seqsy, decoded_results)
    #print(len(decoded_results))
    return decoded_results    
if __name__ == '__main__':
    seqsy = parse_fasta(input("Please write the name of the fasta file you want to predict: "))
    windowz = windowmaking(seqsy, 25)
    int_wind = window_int(windowz)
    sequence_in_windows = onehot(int_wind)
    predict(sequence_in_windows, seqsy)
    
