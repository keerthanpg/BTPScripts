import os
import json
import math

os.chdir('C:\Users\KEERTHANA\Desktop\BTPScripts')
data1=[]
dist=[]

with open('C:\Users\KEERTHANA\Desktop\BTPScripts\dataupdate.txt', 'r') as datafile:
    data1=json.load(datafile)



for element in data1:
    distthis={}
    distthis['Name']=element['Name']
    facesize=(element['height']**2+ element['width']**2)**(0.5)
    distthis['EyetoEye']=(((element['rightEyeCenterX']-element['leftEyeCenterX'])**(2)+(element['rightEyeCenterY']-element['leftEyeCenterY'])**(2))**(0.5))*100/facesize
    distthis['EyebrowtoEye']=(((element['rightEyeBrowMiddleX']-element['leftEyeBrowMiddleX'])**(2)+(element['rightEyeBrowMiddleY']-element['leftEyeBrowMiddleY'])**(2))**(0.5))*100/facesize
    distthis['BrowBridge']=(((element['rightEyeBrowLeftX']-element['leftEyeBrowRightX'])**(2)+(element['rightEyeBrowLeftY']-element['leftEyeBrowRightY'])**(2))**(0.5))*100/facesize
    distthis['LengthofMouth']=(((element['lipCornerRightX']-element['lipCornerLeftX'])**(2)+(element['lipCornerRightY']-element['lipCornerLeftY'])**(2))**(0.5))*100/facesize
    distthis['NoseTiptoLipMid']=(((element['lipLineMiddleX']-element['noseTipX'])**(2)+(element['lipLineMiddleY']-element['noseTipY'])**(2))**(0.5))*100/facesize
    distthis['NoseTiptoLipRight']=(((element['lipCornerRightX']-element['noseTipX'])**(2)+(element['lipCornerRightY']-element['noseTipY'])**(2))**(0.5))*100/facesize
    distthis['NoseTiptoLipLeft']=(((element['lipCornerLeftX']-element['noseTipX'])**(2)+(element['lipCornerLeftY']-element['noseTipY'])**(2))**(0.5))*100/facesize
    distthis['NoseTiptoRightBrowMid']=(((element['rightEyeBrowMiddleX']-element['noseTipX'])**(2)+(element['rightEyeBrowMiddleY']-element['noseTipY'])**(2))**(0.5))*100/facesize
    distthis['NoseTiptoLeftBrowMid']=(((element['leftEyeBrowMiddleX']-element['noseTipX'])**(2)+(element['leftEyeBrowMiddleY']-element['noseTipY'])**(2))**(0.5))*100/facesize
    distthis['NoseLefttoRight']=(((element['nostrilLeftSideX']-element['nostrilRightSideX'])**(2)+(element['nostrilLeftSideY']-element['nostrilRightSideY'])**(2))**(0.5))*100/facesize
    distthis['NoseLength']=(((element['noseBtwEyesX']-element['noseTipX'])**(2)+(element['noseBtwEyesY']-element['noseTipY'])**(2))**(0.5))*100/facesize
    distthis['NoseTiptoChin']=(((element['chinTipX']-element['noseTipX'])**(2)+(element['chinTipY']-element['noseTipY'])**(2))**(0.5))*100/facesize
    distthis['NoseRighttoLipRight']=(((element['lipCornerRightX']-element['nostrilRightSideX'])**(2)+(element['lipCornerRightY']-element['nostrilRightSideY'])**(2))**(0.5))*100/facesize
    distthis['NoseLefttoLipLeft']=(((element['lipCornerLeftX']-element['nostrilLeftSideX'])**(2)+(element['lipCornerLeftY']-element['nostrilLeftSideY'])**(2))**(0.5))*100/facesize    
    dist.append(distthis)

with open('C:\\Users\\KEERTHANA\\Desktop\\BTPScripts\\features.txt', 'w') as outfile:
    json.dump(dist, outfile)
    




