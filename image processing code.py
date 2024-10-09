# -*- coding: utf-8 -*-
"""
Created on Tue May 21 00:12:16 2019

@author: team
"""

#CODE FOR IMAGE PROCESSING OF THE FIRST PARAMETER- SALIVA FERN PATTERN RECOGNITION
#import the required packages
import sys
sys.path.append('/usr/local/lib/python3.5/site-packages')
import cv2
from math import sqrt 
#create a function to detect lines
def detect_lines(imag):
    src=cv2.resize(imag,(554,738))
    gray= cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5,5),0)
    img=cv2.Canny(gray,50,50)
    img=img[245:550,102:450]
    lsd = cv2.createLineSegmentDetector(0)
    lines = lsd.detect(img)[0]
    drawn_img = lsd.drawSegments(img,lines)
    cv2.imshow('detected image',drawn_img)
    cv2.waitKey(0)
return lines

#run the function for a reference image
refimage = "C:/Users/keert/OneDrive/Desktop/final project/standard_test_images/Fern A.jpg"
image1 = cv2.imread(refimage, cv2.IMREAD_COLOR)
#initialize the required variables
ref_len=0
len=0
reflines=detect_lines(image1)
for i in range(reflines.shape[0]):
    x=(abs(reflines[i,0,0])-(reflines[i,0,2]))**2
    y=(abs(reflines[i,0,1])-(reflines[i,0,3]))**2
    z=x+y
    len=sqrt(z) 
 #find the highest line segment length and use that as reflen
   if len>ref_len:
        ref_len=len

#load the test image
testimage = "C:/Users/keert/OneDrive/Desktop/final project/standard_test_images/Fern A.jpg"
image2 = cv2.imread(testimage, cv2.IMREAD_COLOR)
#run the function on the test image
lines=detect_lines(image2)
for i in range(lines.shape[0]):
    x=(abs(lines[i,0,0])-(lines[i,0,2]))**2
    y=(abs(lines[i,0,1])-(lines[i,0,3]))**2
    z=x+y
    len=sqrt(z) 
    if len>ref_len:
        print('fertile period')
        break
    elif len<ref_len and i==(lines.shape[0]-1):
        print('Infertile period')