import numpy as np
input_file = open('test.txt', 'r')

######Making a list of the input file because when making a dictioanry I was scared to lose the order of the sequences. In the list input_list, name, sequence, and topology are listed.
input_list = [(line.strip()) for line in input_file]
name = [element for element in input_list[::3]]
seq = [element for element in input_list[1::3]]
topo = [element for element in input_list[2::3]]   
input_file.close()

aa = '0GALMFWKQESPVICYHRNDT'
aa_to_int = dict((c, i) for i, c in enumerate(aa))
window = int(input('Input window size (must be odd number): '))
padding = window//2


######Making the windows into a window list. Adding X to start and end.
window_list = []
for sequence in seq:
    sequence = ((padding)*'0' + sequence + ((padding)*'0'))
    for residue in range(0, len(sequence)):
        if residue+(window) > len(sequence):
            break
        window_list.append(sequence[residue:residue+window])
    

######Making the aminoacids in the windows to integers
windows_in_integers = []
for window in window_list:
    windows_in_int = [aa_to_int[aa] for aa in window]    
    windows_in_integers.append(windows_in_int)


######One hot encoding windows
onehot_encoded_windows = []
for window in windows_in_integers:
    this_window = []
    for residue in window:
        letter = [0 for _ in range(len(aa))]
        if residue != 0:      
            letter[residue] = 1
        else:
            pass
        this_window.extend(letter)           
    onehot_encoded_windows.append(this_window)


######Encoding burial status
burial = {'E':1, 'B':-1}
burial_decode = {1:'E', -1:'B'}
topology_list = []
for proteins in topo:    
    for topologies in proteins:
        y = burial[topologies]
        topology_list.append(y)


#####Training
from sklearn import svm
np.set_printoptions(threshold=np.inf)
X = onehot_encoded_windows
Y = topology_list
clf = svm.SVC()
clf.fit(X, Y)


#####Testing(on training data)
result = clf.predict(onehot_encoded_windows)
results = list(result)
decoded_results = []
for element in results:
    decoded_results.append(burial_decode[element])
print(results)
print(decoded_results)
    
