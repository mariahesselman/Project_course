import pandas as pd
import numpy as np
from numpy import argmax
def parser(filename):
    dic = {}
    keys = []
    seq = []
    topo = []
    file = open(filename, 'r')
    with file as f:
        for linenumber, line in enumerate(f):            
            if line[0] == '>':
                keys.append(line[1:-1])
            elif linenumber%3 == 1:
                seq.append(line[:-1])
            elif linenumber%3 == 2:
                topo.append(line[:-1])
        for i in range(len(keys)):
            dic[(keys[i])] = (seq[i], topo[i])            
                               
    #print(keys)
    #print(seq)
    #print(topo)
    #print(dic) 
    df = pd.DataFrame(data=dic)
    #print(df)
    sequences = df.loc[0]
    #print(sequences)
    file.close()
    return sequences
def enconde(filename):
#One-hot ecnoding aa alphabet
    
    seq = parser(filename)
    print(seq)
    aa = 'GALMFWKQESPVICYHRNDT'
    aa_to_int = dict((c, i) for i, c in enumerate(aa))
    int_to_aa = dict((i, c) for i, c in enumerate(aa))
    print(aa_to_int)
    #integer_encoded = [aa_to_int[char] for char in seq]
    #print(integer_encoded)


        
if __name__ == '__main__':
    parser('test.txt')            
    enconde('test.txt')        
