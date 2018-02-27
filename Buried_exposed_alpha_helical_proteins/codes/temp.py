from numpy import argmax
import numpy as np

input_file = open('test.txt', 'r')
# Making a list of the input file because when making a dictioanry I was scared to lose the order of the sequences. In the list input_list, name, sequence, and topology are listed.
input_list = [(line.strip()) for line in input_file]
name = [element for element in input_list[::3]]
seq = [element for element in input_list[1::3]]
topo = [element for element in input_list[2::3]]   
input_file.close()

aa = 'GALMFWKQESPVICYHRNDT'
aa_to_int = dict((c, i) for i, c in enumerate(aa))
print(aa_to_int)
window = int(input('Input window size (must be odd number): '))
padding = window//2

'''RIGHT NOW I'M IGNORING THE FIRST AND LAST RESIDUE IN EACH SEQUENCE'''

#Making the windows into a window list.
window_list = []
for sequence in seq:
    for residue in range(len(sequence)):
        if residue > padding and residue < (len(sequence)-padding):
            window_list.append(sequence[residue-padding:padding+1])
        elif residue <= padding: #taking care of left side of sequence
            rightside_window = sequence[:residue + padding +1]
            zeros = window - len(rightside_window)
            window_list.append('0'*zeros + rightside_window) #padding-residue is how many zeros i need in the beginning
        else: #taking care of the right side
            leftside_window = sequence[residue-1:]
            zeros = window - len(leftside_window)
            window_list.append(leftside_window + '0'*zeros)
        #window_list.append(sequence[residue:residue+window])
print(window_list)



#Making the aminoacids in the windows to integers
'''windows_in_integers = []
for window in window_list:
    windows_in_int = [aa_to_int[aa] for aa in window]
    #print(windows_in_integers)
    windows_in_integers.append(windows_in_int)
print(windows_in_integers)
#print(len(windows_in_integers))


#One hot encoding windows
onehot_encoded_windows = []
for window in windows_in_integers:
    this_window = []
    for residue in window:
        #print(residue)
        letter = [0 for _ in range(len(aa))]            
        letter[residue] = 1
        this_window.extend(letter)
    onehot_encoded_windows.append(this_window)'''


#print(len(seq[0]))
#print(len(seq[1]))
#print(len(seq[2]))
print(onehot_encoded_windows)
print(len(onehot_encoded_windows))
print(np.array(onehot_encoded_windows).shape)

burial = {1:'E', 2:'B'}



#when to add padding?
# should all sequences be in same array?
