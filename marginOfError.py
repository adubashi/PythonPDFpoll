# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 02:01:21 2015

@author: aduba_000
"""

import numpy
import math

def calculateMarginOfError(data,zvalue):
    std = numpy.std(data)
    n = len(data)
    rootn = math.sqrt(n)
    return zvalue *  (std/(rootn))
    
    

print calculateMarginOfError([1,2,3],1.41)
    
        