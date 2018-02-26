import pandas as pd
import numpy as np
from numpy import argmax
dic = {}
keys = []

topo = []

'''       
file = open('test.txt', 'r')
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
#print(dic)                                               
file.close()    
#One-hot encoding aa alphabet    
    #print(seq)
    
#print(empty_array)
'''
def parser(filename):

    
    aa = 'GALMFWKQESPVICYHRNDT'
    aa_to_int = dict((c, i) for i, c in enumerate(aa))
    #print(aa_to_int)
#Defining window size
    LISTSEQ = []
    #window = int(input('Input window size (must be odd number): '))
    for i in filename:
        print(i)
        empty_array = [0]*20
        position = aa.index(i)
        empty_array[position] = 1
        LISTSEQ.append(empty_array)
    return LISTSEQ

if __name__ == '__main__':
    seq = ['AWQ', 'AWQ']    
#for k, v in dic.items():
    for element in seq:
        #print(element)
        print(parser(element))
#split sequences into different files and loop inside of each file. In the end i want an array for each sequence of 20  length of sequence. OR use key

#Integer-encoding protein sequences from list(seq)    
'''
    integer_encoded_seq = []
    for item in range(len(seq)):
        integer_encoded = [aa_to_int[char] for char in seq[item]]
        integer_encoded_seq.append(integer_encoded)
    #print(integer_encoded_seq)
#One-hot encoding sequences
    onehot_encoded = list()
    #for value in integer_encoded_seq:
        #letter = [0 for _ in range(len(aa))] ###Not working because integer_encoded_seq is a list of lists.
        #letter[value] = 1
        #onehot_encoded.append(letter)
    #print(onehot_encoded)
'''
    

        
#if __name__ == '__main__':
 #   parser('test.txt')            
#create empty vector, multiply by the window size
