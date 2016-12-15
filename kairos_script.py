import requests
import json
import base64
import os
from PIL import Image

result=[]
headers = {"Content-Type":"application/json", "app_id":"f5dc3b74", "app_key":"fcfd0276d4b17282e5deab9a3501f796"}
proxies = {
  'http': 'http://10.3.100.207:8080',
  'https': 'http://10.3.100.207:8080'
  }

yourpath = 'C:\Users\KEERTHANA\Desktop\jaffeJPG'
for root, dirs, files in os.walk(yourpath, topdown=False):
    for name in files:        
        #print(os.path.join(root, name))
        with open(os.path.join(root, name), "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        payload={"image": encoded_string, "selector": "SETPOSE" }    
        r = requests.post('https://api.kairos.com/detect', data=json.dumps(payload), proxies=proxies, headers=headers)
        diction=json.loads(r.text)['images'][0]['faces'][0]
        diction['Name']=name
        #print diction
        result.append(diction)
        print '\nGot coordinates for' +name
        print result
       
with open('C:\Users\KEERTHANA\Desktop\data.txt', 'w') as outfile:
    json.dump(result, outfile)
    
    
