# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 17:02:37 2015

@author: Continuum

Creates a vector of specified length containing gradient values for testing
"""

def makeGradientVector(length, height):
    ret = [[0 for x in range(width)] for x in range(height)]
        
    
    for x in range(length):
        for y in range(height):
            ret[x][y] = (x + y) * 0.0001 
    return ret