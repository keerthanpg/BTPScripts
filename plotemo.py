import os
import json
import math
import matplotlib.pyplot as plt

os.chdir('C:\Users\KEERTHANA\Desktop\BTPScripts')
data1=[]
dist=[]
distthis={}
x=[1, 2, 3, 4, 5, 6, 7, 8]

j=0
with open('C:\Users\KEERTHANA\Desktop\BTPScripts\\emotionsupdate.txt', 'r') as datafile:
    data1=json.load(datafile)



for distthis in data1:
    i=1
    array=[]
    for [k, v] in distthis.iteritems():
        if k=='Name':
            continue
        else:
            
            array.append(v)            
            i=i+1
    #print array
    #print len(array)
    plt.plot(x,array)
    #break
    
plt.ylabel('emotionscores')
plt.show()
