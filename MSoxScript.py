import requests
import json
import base64
import os
from PIL import Image
import binascii

result=[]
headers = {"Content-Type":"application/octet-stream", "Ocp-Apim-Subscription-Key":"d7e058a8ce5349779b2d8455cacb3e91"}
proxies = {
  'http': 'http://10.3.100.207:8080',
  'https': 'http://10.3.100.207:8080'
  }

yourpath = 'C:\Users\KEERTHANA\Desktop\jaffeJPG'
for root, dirs, files in os.walk(yourpath, topdown=False):
    for name in files:        
        #print(os.path.join(root, name))
        with open(os.path.join(root, name), "rb") as image_file:
            #encoded_string = base64.b64encode(image_file.read())            
            payload=image_file.read()
            #payload=binascii.hexlify(content)
            #print payload
            image_file.close()
        r = requests.post('https://api.projectoxford.ai/emotion/v1.0/recognize', data=payload, proxies=proxies, headers=headers)
        diction=json.loads(r.text)[0]["scores"]
        result.append(diction)
        diction['Name']=name
        print '\nGot coordinates for' +name
              
with open('C:\Users\KEERTHANA\Desktop\emotionscores.txt', 'w') as outfile:
    json.dump(result, outfile)
    
