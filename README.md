# Project_course
# HELLO! IT IS 16:15 ON FRIDAY MARCH 16TH. I'M ALMOST DONE WITH MY CODE BUT NOT YET.
## Predicting burial status of residues in membrane proteins.
My project consists of four main parts:
1. **Training an SVM classifier on my whole dataset.**  
Parsing and training: `Project_course/Buried_exposed_alpha_helical_proteins/codes/parser_i.py`
	* Optimized window size with 5-fold cross-validation. Window size with the best CV score: 23.
	* Prediction on a hidden data set of 50 proteins to calculate metrics such as MCC and confusion matrix.
	* Compared SVM to decision tree and random forest. SVM gave higher CV score and MCC. 
2. **Making a predictor of burial status**  
Predictor: `Project_course/Buried_exposed_alpha_helical_proteins/codes/predict.py`  
Model: `Project_course/Buried_exposed_alpha_helical_proteins/codes/model.sav`  
Example fasta file: `Project_course/Buried_exposed_alpha_helical_proteins/codes/bigfasta.fasta`
	* Uses model saved in training script.
	* Writes results to a 3line file.  
3. **Training an SVM with position specific frequency matrix**  
Parsing and training: `Project_course/Buried_exposed_alpha_helical_proteins/PSIBLAST/scripts/parse_pssm.py`  
	* Ran PSIBLAST with all of my sequences and saved the PSSMs and position specific frequency matrix
	* Trained an SVM using position specific frequency matrices for my whole dataset.
	* Window size 3.  
4. **Predicting burial status from a position specific frequency matrix**  
Predictor for PSSM: `Project_course/Buried_exposed_alpha_helical_proteins/PSIBLAST/scripts/predict_pssm.py`  
Model for PSSM: `Project_course/Buried_exposed_alpha_helical_proteins/PSIBLAST/scripts/pssm_model.sav`  
Bash script: `Project_course/Buried_exposed_alpha_helical_proteins/PSIBLAST/bash/predictmanypssms.sh`  
Example pssm: `Project_course/Buried_exposed_alpha_helical_proteins/PSIBLAST/pssm/>d1du0b_.a.4.1.1.fasta.pssm`  
	* Takes **one** PSSM file and parses it and predicts the burial status of each position.
	* Results are written to file.	
	* Bash script can be used to run on many pssm files.


