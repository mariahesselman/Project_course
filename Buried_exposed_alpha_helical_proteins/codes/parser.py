import pandas as pd
import numpy as np
from numpy import argmax
dic = {}
keys = []
seq = []
topo = []

def parser(filename):    
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
    print(dic)                                               
    file.close()    
#One-hot ecnoding aa alphabet    
    print(seq)
    aa = 'GALMFWKQESPVICYHRNDT'
    aa_to_int = dict((c, i) for i, c in enumerate(aa))
    print(aa_to_int)
#Defining window size
    window = int(input('Input window size (must be odd number): '))
#Integer-encoding protein sequences from list(seq)    
    integer_encoded_seq = []
    for item in range(len(seq)):
        integer_encoded = [aa_to_int[char] for char in seq[item]]
        integer_encoded_seq.append(integer_encoded)
    print(integer_encoded_seq)
    

        
if __name__ == '__main__':
    parser('test.txt')            
       
