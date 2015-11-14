# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 13:52:35 2015

@author: Continuum
"""

import scipy
from PIL import Image
import randomVector
import toRGB
def WriteToImage(vec):
    vec = randomVector.randNormalArray(640*480)
    

    im = Image.new("RGB",(640,480),"white" )


    for i in range(480):
        for j in range(640):
            pix = toRGB.returnColorValue(vec[j+(i*640)])
            print(vec[j+(i*640)])
            im.im.putpixel((j, i),pix)


    im.save("outfile.png")
    print("done")