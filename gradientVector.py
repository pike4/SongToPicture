# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 17:02:37 2015

@author: Continuum

Creates a vector of specified length containing gradient values for testing
"""

def makeGradientVector(length):
    ret = []
    for x in range(length):
        ret.append((x * .000003))
    return ret