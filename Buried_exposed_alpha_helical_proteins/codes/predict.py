from sklearn.externals import joblib
import numpy as np
import pickle

loaded_model = pickle.load(open('model.sav', 'rb'))
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
    return id_list, seq_list


def windowmaking(seq, window):
    padding = window//2
    padded_sequences = []
    window_list = []    
    for sequence in seq:
        sequence = ((padding*'0') + sequence + (padding*'0'))
        this_wind = []
        for residue in range(len(sequence)):
            if residue+(window) > len(sequence):
                break
            this_wind.append(sequence[residue:residue+window])
        window_list.append(this_wind)
    return window_list


def window_int(windows): 
    windows_in_integers = []
    for sequence in windows:
        temp = []
        for window in sequence:
            windows_in_int = [AA_TO_INT[aa] for aa in window]    
            temp.append(windows_in_int)
        windows_in_integers.append(temp)
    return windows_in_integers    


def onehot(int_wind): 
    onehot_encoded_windows = []
    for sequence in int_wind:
        this_sequence = []
        for window in sequence:
            this_window = []
            for residue in window:
                letter = [0 for _ in range(len(aa))]
                if residue != 0:      
                    letter[residue] = 1
                else:
                    pass
                this_window.extend(letter)
            this_sequence.append(this_window)
        onehot_encoded_windows.append(this_sequence)
    return onehot_encoded_windows    


def predict(sequence_in_windows):
    result_list = []
    for sequence in sequence_in_windows:
        result = loaded_model.predict(sequence)
        result_list.append(result)
    burial_decode = {1:'E', -1:'B'}
    decoded_results = []
    for sequence in result_list:
        seq_decode = []
        for topology in sequence:
            seq_decode.append(burial_decode[topology])
        decoded_results.append(seq_decode)    
    return decoded_results


def results(topology, id_, seq):
    string_topo = []    
    for element in topology:
        string_topo.append(''.join(element))
    with open('Results.3line.txt', 'w') as f:
        for element in range(len(id_)):
            f.write(id_[element] + '\n')
            print(id_[element])
            f.write(seq[element] + '\n')
            print(seq[element])
            f.write(string_topo[element] + '\n')
            print(string_topo[element])
        f.close()
    print('Results available in ./Results.3line.txt')


if __name__ == '__main__':
    id_, seq = parse_fasta('bigfasta.fasta')
    windowz = windowmaking(seq, 23)
    int_wind = window_int(windowz)
    sequence_in_windows = onehot(int_wind)
    topology = predict(sequence_in_windows)
    results(topology, id_, seq)    
