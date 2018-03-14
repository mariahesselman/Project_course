# Project_course
##Predicting burial status of residues in membrane proteins.
My project consists of three main parts:
1. **Training an SVM classifier on my whole dataset.** 
Parsing and training: `Project_course/Buried_exposed_alpha_helical_proteins/codes/parser_i.py`
	* Optimized window size with 5-fold cross-validation. Window size with the best CV score: 23.
	* Prediction on a hidden data set of 50 proteins to calculate metrics such as MCC and confusion matrix.
	* Compared SVM to decision tree and random forest. SVM gave higher CV score and MCC. 
2. **Making a predictor of burial status**
Predictor: `Project_course/Buried_exposed_alpha_helical_proteins/codes/predict.py`
Model: `Project_course/Buried_exposed_alpha_helical_proteins/codes/model.sav`
	* Uses model saved in training script.
	* Writes results to a 3line file.





The script where I trained and saved the model is: 
Project_course/Buried_exposed_alpha_helical_proteins/codes/parser_i.py

The mean cross validation score with a window size of 23 is: 0.72 

To use my model to predict the burial status of residues in sequences in a fasta file, you need the following files in the same directory:

1. 
2. 


When running predict.py , you will be prompted to enter the name of a fasta file contianing sequences whose topology you want to predict. The fasta file that I used to test whether this worked is Project_course/Buried_exposed_alpha_helical_proteins/codes/bigfasta.fasta

Note that the sequences in your fasta file should span one line each only (not like old fasta files).

After running predict.py your results will be available in ./Results.3line.txt

