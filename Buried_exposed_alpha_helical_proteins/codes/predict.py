"""Takes in a fasta file and predicts the topology for sequences in the file"""
import pickle


LOADED_MODEL = pickle.load(open('./models/optimized_model.sav', 'rb'))
AA = '0GALMFWKQESPVICYHRNDT'
AA_TO_INT = dict((c, i) for i, c in enumerate(AA))


def parse_fasta(filename):
    """Takes fasta file and parses information to lists"""
    input_file = open(filename, 'r')
    id_list = []
    seq_list = []
    for line in input_file:
        if line.startswith('>'):
            id_list.append(line.strip())
        else:
            seq_list.append(line.strip())
    return id_list, seq_list


def windowmaking(sequences, window):
    """Makes windows and adds padding"""
    padding = window//2
    window_list = []
    for sequence in sequences:
        sequence = ((padding*'0') + sequence + (padding*'0'))
        this_wind = []
        for residue in range(len(sequence)):
            if residue+(window) > len(sequence):
                break
            this_wind.append(sequence[residue:residue+window])
        window_list.append(this_wind)
    return window_list


def window_int(windows):
    """Converts windows to integers"""
    windows_in_integers = []
    for sequence in windows:
        temp = []
        for window in sequence:
            windows_in_int = [AA_TO_INT[AA] for AA in window]
            temp.append(windows_in_int)
        windows_in_integers.append(temp)
    return windows_in_integers


def onehot(integer_windows):
    """One-hot encodes windows"""
    onehot_encoded_windows = []
    for sequence in integer_windows:
        this_sequence = []
        for window in sequence:
            this_window = []
            for residue in window:
                letter = [0 for _ in range(len(AA))]
                if residue != 0:
                    letter[residue] = 1
                else:
                    pass
                this_window.extend(letter)
            this_sequence.append(this_window)
        onehot_encoded_windows.append(this_sequence)
    return onehot_encoded_windows


def predict(sequence_in_windows):
    """Predicts topology of sequence"""
    result_list = []
    for sequence in sequence_in_windows:
        result = LOADED_MODEL.predict(sequence)
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
    """Writes results to file"""
    string_topo = []
    for element in topology:
        string_topo.append(''.join(element))
    with open('../result_files/predictions/Results.3line.txt', 'w') as f:
        for element in range(len(id_)):
            f.write(id_[element] + '\n')
            print(id_[element])
            f.write(seq[element] + '\n')
            print(seq[element])
            f.write(string_topo[element] + '\n')
            print(string_topo[element])
        f.close()
    print('Results available in ../result_files/predictions/')


if __name__ == '__main__':
    ID, SEQ = parse_fasta('../datasets/bigfasta.fasta')
    WINDOWZ = windowmaking(SEQ, 23)
    INT_WIND = window_int(WINDOWZ)
    SEQUENCE_IN_WINDOWS = onehot(INT_WIND)
    TOPOLOGY = predict(SEQUENCE_IN_WINDOWS)
    results(TOPOLOGY, ID, SEQ)
