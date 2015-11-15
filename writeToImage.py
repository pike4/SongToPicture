# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 13:52:35 2015

@author: Continuum

Takes a vector of <= 1 length values and writes them to the image
"""


from PIL import Image
from uuid import uuid4
import randomVector
import gradientVector
import convertToRGB

def WriteToImage(vec):
    #Test vectors
    #vec = randomVector.randNormalArray(640, 480)
    #vec = gradientVector.makeGradientVector(1440*1080)
    
    width = len(vec[0])
    height = len(vec)
    
    slicesPerSecond = 20
    
    #Output file
    im = Image.new("RGB",(width,height + 70),"white" )

    #Write each individual pixel to file
    for i in range(width):
        for j in range(height):
            pix = convertToRGB.returnRGB(vec[j][i])
            #print(vec[j+(i*640)])
            im.im.putpixel((i,j),pix)
    for k in range(width):
        for l in range(70):
            im.im.putpixel((k, height + l), (255,255,255))
            
    for minMarks in range(int(width / (slicesPerSecond * 60 ))+1):
        if (width / (slicesPerSecond * 60)) < width:
           for minMarkLength in range(70):
              im.im.putpixel((int(minMarks * slicesPerSecond * 60),int(height + minMarkLength)), (0, 0, 0))
               
           
    for secMarks in range(int(width / slicesPerSecond)):
       for secMarkLength in range(12):
           im.im.putpixel((int(secMarks * slicesPerSecond),int(height + secMarkLength)), (0,0,0))
           
    for secMarks15 in range(int(width / (slicesPerSecond * 15))):
       for secMarkLength15 in range(40):
           im.im.putpixel((int(secMarks15 * slicesPerSecond * 15),int(height + secMarkLength15)), (0,0,0))
           
    for secMarks5 in range(int(width / (slicesPerSecond * 5))):
       for secMarkLength5 in range(25):
           im.im.putpixel((int(secMarks5 * slicesPerSecond * 5),int(height + secMarkLength5)), (0,0,0))
        
        
            
    fileName = "photos\\" + str(uuid4()) + ".png"
    #FILENAME = fileName.concat(".png")

    im.save(fileName)

    
    print("done :" + fileName)