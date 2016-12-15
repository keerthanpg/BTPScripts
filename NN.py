from sknn.mlp import Classifier, Layer
import os
import json
import math
os.chdir('C:\Users\KEERTHANA\Desktop\BTPScripts')
data1=[]
data2=[]
dist=[]
distthis={}
xrow=[]
yrow=[]
x=[]
y=[]


with open('C:\Users\KEERTHANA\Desktop\BTPScripts\\features.txt', 'r') as datafile:
    data1=json.load(datafile)


for distthis in data1:
    for key in distthis:
        if key=='Name':
            continue
        else:
            xrow.append(distthis[key])
    x.append(xrow)

datafile.close()

with open('C:\Users\KEERTHANA\Desktop\BTPScripts\\emotionsupdate.txt', 'r') as datafile:
    data2=json.load(datafile)


for distthis in data2:
    for key in distthis:
        if key=='Name':
            continue
        else:
            yrow.append(distthis[key])
    y.append(yrow)

datafile.close()

X_train=x[0:151]
Y_train=y[0:151]
X_valid=x[151:166]
X_train=x[166:182]
Y_valid=y[151:166]
Y_train=y[166:182]

    
nn = Classifier(
    layers=[
        Layer("Rectifier", units=100),
        Layer("Softmax")],
    learning_rate=0.02,
    n_iter=10)
nn.fit(X_train, Y_train)

Y_valid = nn.predict(X_valid)

score = nn.score(X_test, Y_test)






