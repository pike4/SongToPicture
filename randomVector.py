# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 14:59:56 2015

@author: Continuum
"""
import random
def randNormalArray(len):
    ret = []
    random.seed()
    for x in range(len):
        ret.append((random.randrange(10)/10) +0.1)
    return ret