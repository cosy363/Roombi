from sklearn.linear_model import LogisticRegression
import joblib
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
import pickle

print("yeah")
data = pd.read_csv('data.csv', names=['Score', 'Category', 'Color'])

x,y = [],[]
for i in range(1000):
    x.append([data['Category'][i],data['Color'][i]]) 
    y.append(data['Score'][i])

softmax_reg = LogisticRegression(multi_class="multinomial",solver="lbfgs", C=10, random_state=42)
softmax_reg.fit(x, y)

joblib.dump(softmax_reg, 'model.joblib')

model = joblib.load('model.joblib') 

score = model.predict_proba([[1234, 1324]])
score = score[0][0] + score[0][1]*2 + score[0][2]*3 + score[0][3]*4
print(score)