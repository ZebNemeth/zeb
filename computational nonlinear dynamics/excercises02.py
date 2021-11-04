# Author: Zeb Németh
# Purpose: Course material excercises from Santa Fé's online course,

# "Nonlinear Dynamics: Mathematical and Computational Approaches"
# https://www.complexityexplorer.org/courses/136-nonlinear-dynamics-mathematical-and-computational-approaches

# Date created: around autumn 2020

# Chapter 2 excercises and sandbox

import numpy as np
import matplotlib.pyplot as plt
import time



def logistic( x, R ):                   # to keep the amount of operators low, and language high
    return R*x*( 1-x ) 

def xTrajLogistic( x, R, N ):                   # generates a full trajectory of x_n as array
    xTraj = []
    for i in range( N ):
        xTraj.append( logistic( x, R ) )
        x = logistic( x, R )
    return xTraj

# ---- Question 1 ----
# Write a function that plots a bifurcationdiagram for the logistic map.
# It must take as arguments:
# x0, rMin, rMax, rSteps, nTotalIterates, nDiscardIterates

def bifDiagram( initX, minR, maxR, nStepsR, nIterations, nKeep ):
    stepSizeR = ( maxR-minR )/nStepsR
    xCoords = []
    nCoords = []

    for i in range ( nStepsR-1 ):
        R = minR+( i*stepSizeR )        
        xCoords.extend( xTrajLogistic(initX, R, nIterations)[-nKeep:] ) # we extend, not append, the xCoordinates with the last nKeep elements of the full trajectory

        for i in range ( nKeep ): # and give each of the new x-values kept its appropriate, same R-value
            nCoords.append( R )
    return nCoords, xCoords

# x,y = bifDiagram( .2, 3.5699, 3.57, 1000, 300000, 2048 )
# plt.scatter( x, y, s=0.01)
# plt.show()

# x,y = bifDiagram( .2, 3.84, 3.8571, 500, 2048, 1024 )
# plt.scatter( x, y, s=0.01)
# plt.show()

# ---- Questions in 2.4 ----

# for a), b), c) and d), just zoom in on the plot from question above

# e)

'''
b1 = 3
b2 = 3.4494897
b3 = 3.5440903
'''
def deltaN(b1,b2,b3):
    return ( b2-b1 )/( b3-b2 )
'''
print ( deltaN( b1, b2, b3 ) )


b3 = 3.544090
b4 = 3.564406
b5 = 3.568759
print ( deltaN( b2, b3, b4 ) )
print ( deltaN( b3, b4, b5 ) )

b6 = 3.569691
b7 = 3.569891
print ( deltaN( b4, b5, b6 ) )
print ( deltaN( b5, b6, b7 ) )

b8 = 3.569934
b9 = 3.5699431
print ( deltaN( b6, b7, b8 ) )
print ( deltaN( b7, b8, b9 ) )

b10 = 3.56994514
print ( deltaN( b8, b9, b10 ) )
'''
# ---- Question 2 ----
# I just zero'd in to smaller ranges of R, now to [3.5699, 3.57].
# More important than steps is iterations, and adjusting kept trajectory points to the
# power of amount of bifurcations (b8 = 2^nBifurcations = 2^8 = 256, b10 = 1024)

# ---- Question 3 ----
def rMinXsq( x, R ):
    return ( R - (x*x) )

def xTrajRMinXsq( x, R, N ):                   # generates a full trajectory of x_n as array
    xTraj = []
    for i in range( N ):
        x = rMinXsq( x, R )
        xTraj.append( x )
    return xTraj
def bifDiagramRMinXsq( initX, minR, maxR, nStepsR, nIterations, nKeep ):
    stepSizeR = ( maxR-minR )/nStepsR
    xCoords = []
    nCoords = []

    for i in range ( nStepsR-1 ):
        R = minR+( i*stepSizeR )        
        xCoords.extend( xTrajRMinXsq(initX, R, nIterations)[-nKeep:] ) # we extend, not append, the xCoordinates with the last nKeep elements of the full trajectory

        for i in range ( nKeep ): # and give each of the new x-values kept its appropriate, same R-value
            nCoords.append( R )
    return nCoords, xCoords

# x,y = bifDiagramRMinXsq( .2, 1.4008, 1.4014, 200, 300000, 256 )
# plt.scatter( x, y, s=0.01)
# plt.show()
'''
b = [ 0.75, 1.25, 1.368, 1.394, 1.3996, 1.4008, 1.4010, 1.401085, 1.401139]
for i in range( len(b)-2 ):
    print ( deltaN( b[i], b[i+1], b[i+2] )/4.6692016 )
'''
# Starts off closing in, then transient lengt starts taking over and didn't feel like
# doing the same precision-work as above. So yes, and yes.

# ---- Question 4 ----
# z <> z² + c is close to above, but c=r and z²=-x². That minus sign may change things...

def julia(z, c):
    return ( z*z + c)


def xMapTraj( map, x, R, N):                   # generates a full trajectory of x_n as array
    xTraj = []
    for i in range( N ):
        x = map( x, R )
        xTraj.append( x )
    return xTraj

def printProgress(current, total, tBegin, tEnd=0):
    secondsLeft=int(-(current-total)*(tEnd-tBegin)/1000000000)
    minutesLeft= str(secondsLeft//60)
    restOfSeconds= str(secondsLeft%60)
    underTen = ""
    if ( secondsLeft%60 <= 9 ):
        underTen = "0"

    print("   "+str(current)+"/"+str(total)+", est. time remaining: "+minutesLeft+":"+underTen+restOfSeconds, end= "\r")




def bifDiagramMap( map, initX, minR, maxR, nStepsR, nIterations, nKeep ):
    stepSizeR = ( maxR-minR )/nStepsR
    xCoords = []
    nCoords = []
    for i in range ( nStepsR-1 ):
        tBegin=time.time_ns()
        
        R = minR+( i*stepSizeR )        
        xCoords.extend( xMapTraj( map, initX, R, nIterations)[-nKeep:] ) # we extend, not append, the xCoordinates with the last nKeep elements of the full trajectory
        tEnd=time.time_ns()
        printProgress(i, nStepsR, tBegin, tEnd)
        for i in range ( nKeep ): # and give each of the new x-values kept its appropriate, same R-value
            nCoords.append( R )

        tEnd=time.time_ns()
        


        
    return nCoords, xCoords






# ---- Viewing a plot using certain parameters ----

usedMap = julia
usedInitX = .3
usedMinR = -1.5172 # between -1.2 and
usedMaxR = -1.5206 # -1.75 are a full overview of the interesting area
usedNStepsR = 500
usedNIterations = 300000
nKeep = 16000      # !!!!! High nKeep makes for a density plot when paired with small marker size (below 1, markers become transparent)



tBegin = time.time_ns()
x, y = bifDiagramMap( julia, usedInitX, usedMinR, usedMaxR, usedNStepsR, usedNIterations, nKeep)
tEnd = time.time_ns()
print( str( (tEnd - tBegin) / 1000000000 ) + " seconds for calculating coördinates" )


tBegin=time.time_ns()
plt.scatter( x, y, marker='$*$', s=.01, linewidths=0)
tEnd = time.time_ns()
print( str( (tEnd - tBegin) / 1000000000 ) + " seconds for making plot" )


tBegin=time.time_ns()
plt.show()
tEnd = time.time_ns()
print( str( (tEnd - tBegin) / 1000000000 ) + " seconds spent viewing plot" )


tBegin=time.time_ns()
plt.savefig('JuliaBifDiagram Test.png', dpi = 2500)
tEnd = time.time_ns()
print( str( (tEnd - tBegin) / 1000000000 ) + " seconds for writing plotimage to png" )

