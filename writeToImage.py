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
    
    #Output file
    im = Image.new("RGB",(width,height),"white" )

    #Write each individual pixel to file
    for i in range(width):
        for j in range(height):
            pix = convertToRGB.returnRGB(vec[j][i])
            #print(vec[j+(i*640)])
            im.im.putpixel((i,j),pix)

    
    fileName = "photos\\" + str(uuid4()) + ".png"
    #FILENAME = fileName.concat(".png")

    im.save(fileName)

    
    print("done :" + fileName)