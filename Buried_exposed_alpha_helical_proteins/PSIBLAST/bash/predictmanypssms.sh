cd ../predictpssm/
for file in *.fasta.pssm

do 
python3 ../scripts/predict_pssm.py $file #write directory
done
