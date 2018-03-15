import parser_i

milda = '../datasets/hidden_set.3line.txt'
mysequences = '../datasets/dataset'

mynames = parser_i.parse_name(mysequences)
myseqs = parser_i.parse_seq(mysequences)

mildasnames = parser_i.parse_name(milda)
mildasseqs = parser_i.parse_seq(milda)
mildastop = parser_i.parse_topo(milda)
mildasdic = {mildasnames[element]:(mildasseqs[element], mildastop[element]) for element in range(len(mildasnames))}
#print(mildasdic)

newseqs = open('../datasets/hidden.fasta', 'w')
for element in range(len(mildasnames)):
    newseqs.write(mildasnames[element] + '\n')
    newseqs.write(mildasseqs[element] + '\n')
    
myy = open('../datasets/myseqs', 'w')
for element in range(len(mynames)):
    myy.write(mynames[element] + '\n')
    myy.write(myseqs[element] + '\n')
    
ids = open('../datasets/blinddataset_id.txt', 'r')
lines = ids.readlines()

f = open('../datasets/50hidden.3line.txt', 'r+')

for line in lines:
    line = '>' + line.strip()
    if line in mildasdic:       
        f.write(line + '\n')
        f.write(mildasdic[line][0] + '\n')
        f.write(mildasdic[line][1] + '\n')
fi = '../datasets/50hidden.3line.txt'
hiddennames = parser_i.parse_name(fi)
hiddenseqs = parser_i.parse_seq(fi)
# making sure that the hidden 50 are not in my trainin dataset.
for element in range(len(mynames)):
    if mynames[element] == hiddennames[element]:
        print(warning)

fasta = open('../datasets/50hidden.fasta', 'w')
for element in range(50):
    fasta.write(hiddennames[element] + '\n')
    fasta.write(hiddenseqs[element] + '\n')
