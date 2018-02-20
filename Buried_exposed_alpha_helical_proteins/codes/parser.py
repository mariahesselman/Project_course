import pandas as pd
def parser(testfile):
    dic = {}
    keys = []
    seq = []
    topo = []
    file = open(testfile, 'r')
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
    print(df)
parser('buried_exposed_alpha.3line.txt')
        
            
            
