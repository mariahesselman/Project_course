"""Writing prediction scores of hidden set to file"""
import numpy as np
from sklearn.metrics import matthews_corrcoef
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import predict
import parser_i


predictedtopo =[]
burial = {'E':1, 'B':-1}
topo = parser_i.parse_topo('../result_files/predictions/opt_pred_50hidden.3line.txt')
for proteins in topo:    
    for topologies in proteins:
        y = burial[topologies]
        predictedtopo.append(y)

realtopo = []
topo = parser_i.parse_topo('../datasets/50hidden.3line.txt')
for proteins in topo:
    prot = []    
    for topologies in proteins:
        y = burial[topologies]
        realtopo.append(y)

print('Calculating scores')
svm_classreport = classification_report(realtopo, predictedtopo, labels = [1, -1])
svm_confusionm = confusion_matrix(realtopo, predictedtopo, labels = [1, -1])
random_mcc = matthews_corrcoef(realtopo, predictedtopo)

report = open('../result_files/opt_accuracyreport50.txt', 'w')
report.write('Classification report:' + '\n' + str(svm_classreport) + '\n')
report.write('Confusion matrix:' + '\n' + str(svm_confusionm) + '\n')
report.write('MCC:' + str(random_mcc))
report.close()
