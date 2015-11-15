# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 14:59:56 2015

@author: Continuum

Creates a vector of specified length containing normalilzed length values
"""
import random
def randNormalArray(width, height):
    ret = [[0 for i in range(height)] for j in range(width)]
    random.seed()
    for x in range(width):
        for y in range(height):
            print('a')
            ret[x][y] = (random.randrange(1000)/1000)
    return ret