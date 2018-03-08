# Project_course
I have trained a model with my whole dataset and a window size of 23 since 23 gave me the highest cross validation score (when doing 3 fold cross validation of window sizes from 3 to 35). 

The script where I trained and saved the model is: 
Project_course/Buried_exposed_alpha_helical_proteins/codes/parser_i.py

The mean cross validation score with a window size of 23 is: 0.72 

To use my model to predict the burial status of residues in sequences in a fasta file, you need the following files in the same directory:

1. Project_course/Buried_exposed_alpha_helical_proteins/codes/model.sav
2. Project_course/Buried_exposed_alpha_helical_proteins/codes/predict.py

When running predict.py , you will be prompted to enter the name of a fasta file contianing sequences whose topology you want to predict.

After running predict.py your results will be available in ./Results.3line.txt

