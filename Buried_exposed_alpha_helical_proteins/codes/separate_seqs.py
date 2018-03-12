import parser_i
# takes my dataset and makes one fasta file with each sequence for PSI BLAST.
def saveprots(dataset):
    names = parser_i.parse_name(dataset)
    sequences = parser_i.parse_seq(dataset)
    
    for j in range(len(names)):        
        outfile = open("../PSIBLAST/fastafiles/" + names[j] + ".fasta", "w")
        outfile.write(names[j] + '\n')
        outfile.write(sequences[j] + '\n')
        outfile.close()
saveprots('dataset')
