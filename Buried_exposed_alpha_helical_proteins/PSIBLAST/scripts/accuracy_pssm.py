"""Writing prediction scores of hidden sequence to file"""
import sys
import numpy as np
from sklearn.metrics import matthews_corrcoef
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
sys.path.insert(0, "../../codes")
import parser_i


predictedtopo =[]
burial = {'E':1, 'B':-1}
prediction = (open('../pssm_svm_predictions.txt', 'r')).readlines()
topo_pred = prediction[1].strip()

    
for topologies in topo_pred:
    y = burial[topologies]
    predictedtopo.append(y)

realtopo = []
topo = parser_i.parse_topo('../real_topo_testing_pred.3line.txt')
   
for proteins in topo:
    prot = []    
    for topologies in proteins:
        y = burial[topologies]
        realtopo.append(y)

print('Calculating scores')
svm_classreport = classification_report(realtopo, predictedtopo, labels = [1, -1])
svm_confusionm = confusion_matrix(realtopo, predictedtopo, labels = [1, -1])
random_mcc = matthews_corrcoef(realtopo, predictedtopo)

report = open('../pssm_accuracyreport.txt', 'w')
report.write('Classification report:' + '\n' + str(svm_classreport) + '\n')
report.write('Confusion matrix:' + '\n' + str(svm_confusionm) + '\n')
report.write('MCC:' + str(random_mcc))
report.close()
