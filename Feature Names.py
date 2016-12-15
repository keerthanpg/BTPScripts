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

for distthis in data1:
    for key, value in distthis.iteritems() :
        print key
    break
