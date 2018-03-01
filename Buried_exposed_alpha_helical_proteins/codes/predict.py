import parser_i
from sklearn.externals import joblib
import numpy as np
parser_i.onehot('receptor.txt', 31, 'SVM_input_receptor')
loaded_model = joblib.load('model.sav')
loaded_x = np.load('SVM_input_receptor.npz')
result = loaded_model.predict(loaded_x)
print(result)
