import os
import json
import math

os.chdir('C:\Users\KEERTHANA\Desktop\BTPScripts')
data1=[]
dist=[]
distthis={}
j=0
with open('C:\Users\KEERTHANA\Desktop\BTPScripts\\features.txt', 'r') as datafile:
    data1=json.load(datafile)

fp=open('C:\\Users\\KEERTHANA\\Desktop\\BTPScripts\\featuresarraytrain.txt', 'w')

for distthis in data1:
    
    fp.write('\n')
        
    for key in distthis:
        if key=='Name':
            continue
        else:            
            fp.write(str(distthis[key]))
            fp.write(' ')


    j=j+1
    
fp.close()




