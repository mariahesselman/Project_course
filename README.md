# Project_course
I have trained a model with my whole dataset and a window size of 23 since 23 gave me the highest cross validation score (when doing 3 fold cross validation of window sizes from 3 to 35). 

The script where I trained and saved the model is: 
Project_course/Buried_exposed_alpha_helical_proteins/codes/parser_i.py

The mean cross validation score with a window size of 23 is: 0.72 

To use my model to predict the burial status of residues in sequences in a fasta file, you need the following files in the same directory:

1. Project_course/Buried_exposed_alpha_helical_proteins/codes/model.sav
2. Project_course/Buried_exposed_alpha_helical_proteins/codes/predict.py

<<<<<<< HEAD
When running predict.py , you will be prompted to enter the name of a fasta file contianing sequences whose topology you want to predict. The fasta file that I used to test whether this worked is Project_course/Buried_exposed_alpha_helical_proteins/codes/bigfasta.fasta

=======
When running predict.py , you will be prompted to enter the name of a fasta file contianing sequences whose topology you want to predict.
Note that the sequences in your fasta file should span one line each only (not like old fasta files).
>>>>>>> ca8302b4994a53f360dc3b11f08902719f813c29
After running predict.py your results will be available in ./Results.3line.txt

