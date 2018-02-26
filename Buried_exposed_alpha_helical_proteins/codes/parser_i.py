from numpy import argmax
input_file = open('test.txt', 'r')
# Making a list of the input file because when making a dictioanry I was scared to lose the order of the sequences. In the list input_list, name, sequence, and topology are listed.
input_list = [(line.strip()) for line in input_file]
name = [element for element in input_list[::3]]
seq = [element for element in input_list[1::3]]
topo = [element for element in input_list[2::3]]   
input_file.close()

aa = 'XGALMFWKQESPVICYHRNDT'
aa_to_int = dict((c, i) for i, c in enumerate(aa))
print(aa_to_int)
window = int(input('Input window size (must be odd number): '))
padding = window//2

#Making the windows into a window list. Adding X to start and end.
window_list = []
for sequence in seq:
    sequence = ((padding)*'X' + sequence + ((padding)*'X'))
    print(sequence)
    for residue in range(0, len(sequence)):
        if residue+(window) > len(sequence):
            break
        window_list.append(sequence[residue:residue+window])
#print(window_list)    


#Making the aminoacids in the windows to integers
windows_in_integers = []
for window in window_list:
    windows_in_int = [aa_to_int[aa] for aa in window]
    #print(windows_in_integers)
    windows_in_integers.append(windows_in_int)
#print(windows_in_integers)
#print(len(windows_in_integers))
#print(windows_in_integers[45])

#One hot encoding windows
onehot_encoded_windows = []
for window in windows_in_integers:
    for residue in window:
        #print(residue)
        letter = [0 for _ in range(len(aa))]
        if residue != 0:      
            letter[residue] = 1
        else:
            pass
        onehot_encoded_windows.append(letter)
print(len(seq[0]))
print(len(seq[1]))
print(len(seq[2]))
#print(onehot_encoded_windows)
print(len(onehot_encoded_windows))

burial = {1:'E', 2:'B'}

    
