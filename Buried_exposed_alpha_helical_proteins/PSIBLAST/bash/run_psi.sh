cd ../fastafiles/
for file in *.fasta
do 
#echo $file
psiblast -query $file -evalue 0.001 -db /home/u2353/Bioinfo_course/uniref50.fasta -num_iterations 3 -out ../psi_out/$file -out_ascii_pssm ../pssm/$file.pssm -num_threads=8
done
