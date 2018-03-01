import numpy as np
aa = '0GALMFWKQESPVICYHRNDT'
aa_to_int = dict((c, i) for i, c in enumerate(aa))

def parse_name(dataset):
    input_file = open(dataset, 'r')
    input_list = [(line.strip()) for line in input_file]
    name = [element for element in input_list[0::3]]       
    input_file.close()
    return(name)

def parse_seq(dataset):
    input_file = open(dataset, 'r')
    input_list = [(line.strip()) for line in input_file]
    seq = [element for element in input_list[1::3]]
    input_file.close()
    return(seq)

def parse_topo(dataset):
    input_file = open(dataset, 'r')
    input_list = [(line.strip()) for line in input_file]    
    topo = [element for element in input_list[2::3]]
    input_file.close()
    return(topo)

def windowmaking(dataset, window):
    padding = window//2
    window_list = []
    seq = parse_seq(dataset)
    
    for sequence in seq:
        sequence = ((padding)*'0' + sequence + ((padding)*'0'))
        for residue in range(0, len(sequence)):
            if residue+(window) > len(sequence):
                break
            window_list.append(sequence[residue:residue+window])
    return(window_list)    

######Making the aminoacids in the windows to integers
def window_int(dataset, window): 
    window_list = windowmaking(dataset, window)
    windows_in_integers = []    
    
    for window in window_list:
        windows_in_int = [aa_to_int[aa] for aa in window]    
        windows_in_integers.append(windows_in_int)
    return(windows_in_integers)


######One hot encoding windows
def onehot(dataset, window): 
    windows = window_int(dataset, window)
    onehot_encoded_windows = []
    for window in windows:
        this_window = []
        for residue in window:
            letter = [0 for _ in range(len(aa))]
            if residue != 0:      
                letter[residue] = 1
            else:
                pass
            this_window.extend(letter)           
        onehot_encoded_windows.append(this_window)
    
    burial = {'E':1, 'B':-1}
    burial_decode = {1:'E', -1:'B'}
    topology_list = []
    topo = parse_topo(dataset)
    for proteins in topo:    
        for topologies in proteins:
            y = burial[topologies]
            topology_list.append(y)
    outfile = 'SVM_input.txt'
    np.savez(outfile, x=onehot_encoded_windows, y=topology_list)
    return(onehot_encoded_windows, topology_list)

'''
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
'''

if __name__ == '__main__':
    print(parse_name('test.txt'))
    print(parse_seq('test.txt'))    
    print(parse_topo('test.txt'))    
    print(windowmaking('test.txt', 3))    
    print(window_int('test.txt', 3))    
    onehot('test.txt', 3)
    print(onehot('test.txt', 3))    
    #print(enc_burial('test.txt'))    
        
        
        
        
        
        
        
        
        
        
        
        
