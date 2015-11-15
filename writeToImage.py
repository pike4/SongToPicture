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
import math

def WriteToImage(vec):
    #Test vectors
    vec = randomVector.randNormalArray(1920*1080)
    #vec = gradientVector.makeGradientVector(1440*1080)
    
    width = int(math.sqrt(len(vec)*4/3))
    height = int(len(vec)/width)
    
    #Output file
    im = Image.new("RGB",(width,height),"white" )

    #Write each individual pixel to file
    for i in range(height):
        for j in range(width):
            pix = convertToRGB.returnRGB(vec[j+(i*width)])
            #print(vec[j+(i*640)])
            im.im.putpixel((j, i),pix)

    
    fileName = "photos\\" + str(uuid4()) + ".png"
    #FILENAME = fileName.concat(".png")

    im.save(fileName)

    
    print("done :" + fileName)