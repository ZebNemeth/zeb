# Exponelbrot
# Zeb Németh - 2021-01-31

# Plots Mandelbrot's exponent on z-axis

import numpy as np
import matplotlib.pyplot as plt

def iterate( z, c, exponent ):
    return z**exponent + c

minRe = -4
maxRe = 2
minIm = -2
maxIm = 2
minEx = -3
maxEx = 3
resolutionStep = .01
bailOut = 128


nIterations = 1000

xCoords = []
yCoords = []
zCoords = []


for real in range( minRe, maxRe, resolutionStep ):
    
    for imag in range( minIm, maxIm, resolutionStep):
        for expo in range( minEx, maxEx, resolutionStep):
            c = (real, imag*1j)
            z = c
            for i in range( nIterations ):
                z = iterate( z, c, expo )
                if abs(z) 
            
