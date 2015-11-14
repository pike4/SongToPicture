# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 16:28:54 2015

@author: Continuum
"""

def toWavelength(val):
    if(val > 0 and val < 1):
        return 380 + val * 370
    else:
        return 0