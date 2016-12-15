import os
import json
import math

os.chdir('C:\Users\KEERTHANA\Desktop\BTPScripts')
data1=[]
dist=[]
distthis={}
j=0
with open('C:\Users\KEERTHANA\Desktop\BTPScripts\\emotionsupdate.txt', 'r') as datafile:
    data1=json.load(datafile)

print len(data1)


fp=open('C:\\Users\\KEERTHANA\\Desktop\\BTPScripts\\emotionarraytrain.txt', 'w')

for distthis in data1:
    fp.write('\n')
    j=j+1
    for key in distthis:
        if key=='Name':
            continue
        else:            
            fp.write(str(distthis[key]))
            fp.write(' ')
    '''if j>149:
        break'''

fp.close()

