import os
import json
os.chdir('C:\Users\KEERTHANA\Desktop\BTPScripts')

'''
data1=[]
with open('C:\Users\KEERTHANA\Desktop\BTPScripts\data.txt', 'r') as datafile:
    data1=json.load(datafile)
#print data1[1]
for element in data1:
    for k,v in element.iteritems():
        if v==-1:
            if 'chin' in k:
                print element['Name']
                if (element in data1):
                    data1.remove(element)


with open('C:\Users\KEERTHANA\Desktop\BTPScripts\dataupdate.txt', 'w') as outfile:
    json.dump(data1, outfile)
    '''
data1=[]
with open('C:\Users\KEERTHANA\Desktop\BTPScripts\emotionsupdate.txt', 'r') as datafile:
    data1=json.load(datafile)

print len(data1)
'''
from collections import defaultdict
some_dict = { 'abc':'a', 'cdf':'b', 'gh':'a', 'fh':'g', 'hfz':'g' }
new_dict = defaultdict(list)
for k, v in some_dict.iteritems():
    new_dict[v].append(k)'''
