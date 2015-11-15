# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 14:59:56 2015

@author: Continuum

Creates a vector of specified length containing normalilzed length values
"""
import random
def randNormalArray(len):
    ret = []
    random.seed()
    for x in range(len):
        ret.append((random.randrange(1000)/1000))
    return ret