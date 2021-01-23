

def logisticFunction(x,R):
    return R*x*(1-x)

def logisticIterator(x,R):
    for i in range ( 10 ):
        x = logisticFunction(x,R)
    return x

def logistic( startValue, reproductiveCoefficient, iterations ):
    xN = startValue
    R = reproductiveCoefficient
    
    for i in range ( iterations ):
        xN = logisticFunction( xN, R )

    
    return xN

# ---- 1.2 ----
# ---- Question 1 ----

R = 2.5
x = 0.5
print ( "Data for 1.2.1:")
print ( " ", logisticFunction( logisticFunction( logisticFunction( logisticFunction( x, R ), R ), R ), R ) )
print ( " ", logisticFunction( logisticFunction( logisticFunction( x, R ), R ), R ) ) # Answer
print ( " ", logisticFunction( logisticFunction( x, R ), R ) )
print ( " ", logisticFunction( x, R ) )
print ( x, R )
print ( " ", logisticIterator( x, R ) )

# ---- Question 2 ----
print ( "Data for 1.2.2:" )
print ( " check:  ", logistic( 0.5, 2.5, 3 ) ) # Check
print ( " Answer: ", logistic( 0.2, 2.6, 10 ) ) # Answer

# ---- Question 3 ----
print ( "Data for 1.2.3:" )
print ( " check:  ", logistic( .2, 2, 50 ) )
print ( " Answer: ", logistic( .2, 2.7, 50 ) )



# ---- 1.3 ----
# ---- Question 3 ----
nIterations = 50
startInterval = 0
endInterval = 1
steps = 10
stepSize = (endInterval - startInterval) / (steps-1)

print ( "Data for 1.3.3: ", logistic( .2, 2, nIterations))
for i in range (steps):
    print ( "                ", logistic( startInterval + i*stepSize, 2, nIterations))

# ---- 1.4 ----
# ---- Question 1.4.3 ----
wantToComputeTheAnswerToThisQuestion = False

nIterations = 10000000
startInterval = 2.99999
endInterval = 3.00001
steps = 9
stepSize = (endInterval - startInterval) / (steps-1)

if wantToComputeTheAnswerToThisQuestion :
    print ( "r- value does this qua difference between steps in the limit of iterations: ")
    for i in range (steps):
        print ( "R: " +str(startInterval + i*stepSize) +", limit difference: ", logistic( .5, startInterval + i*stepSize, nIterations) - logistic( .5, startInterval + i*stepSize, nIterations+1)  )
else:
    print ( "Enable boolean for answer of 1.4.4 to see answer (long computation time)" )
# ---- question 1.4.4 ----
nIterations = 1000
startIntervalX = .1
endIntervalX = .9
startIntervalR = 3.2
endIntervalR = 3.2
steps = 9
stepSizeX = (endIntervalX - startIntervalX) / (steps-1)
stepSizeR = (endIntervalR - startIntervalR) / (steps-1)

print ( "Data for 1.4.4:" )
for i in range (steps):
    print ( "                ", sorted( [logistic( startIntervalX + i*stepSizeX, startIntervalR + i*stepSizeR, nIterations), logistic( startIntervalX + i*stepSizeX, startIntervalR + i*stepSizeR, nIterations+1)] ))


# ---- Question 1.4.5 ----
nIterations = 10000
startIntervalX = .5
endIntervalX = .5
startIntervalR = 3.4
endIntervalR = 3.5
steps = 19
stepSizeX = (endIntervalX - startIntervalX) / (steps-1)
stepSizeR = (endIntervalR - startIntervalR) / (steps-1)
nRoundOff = 9
print ( str(logistic(.5, 3.4, 10))[:8] )
print ( "Data for 1.4.5:" )
for i in range (steps):
    print ( "                ", str( sorted([float(str(logistic( startIntervalX + i*stepSizeX, startIntervalR + i*stepSizeR, nIterations))[:nRoundOff+1]),   float(str(logistic( startIntervalX + i*stepSizeX, startIntervalR + i*stepSizeR, nIterations+1))[:nRoundOff+1]),     float(str(logistic( startIntervalX + i*stepSizeX, startIntervalR + i*stepSizeR, nIterations+2))[:nRoundOff+1]),     float(str(logistic( startIntervalX + i*stepSizeX, startIntervalR + i*stepSizeR, nIterations+3))[:nRoundOff+1]),     float(str(logistic( startIntervalX + i*stepSizeX, startIntervalR + i*stepSizeR, nIterations+4))[:nRoundOff+1] ) ]))[1:-1], ","+str(startIntervalR + i*stepSizeR)[:5] )





# ---- Chapter 1 HOMEWORK ----



# ---- Homework 1.a through f ----

import numpy as np
import matplotlib.pyplot as plt

'''
N = 10000
x = np.random.rand(N)
y = np.random.rand(N)

plt.scatter(x,y)
plt.show()
'''
def logisticXarray( startValue, reproductiveCoefficient, iterations ):
    xN = startValue
    R = reproductiveCoefficient
    xArray = []  
    for i in range ( iterations ):
        xArray.append( xN )
        xN = logisticFunction( xN, R )
    return xArray

def plotLogisticDifOverIterations(x1,R1,x2,R2,nIterations=200):
    xOne = np.array([])
    xTwo = np.array([])
    xDif = []
    nIterationsArray = []
    for i in range (nIterations):
        nIterationsArray.append(i)

    xOne = logisticXarray(x1,R1,nIterations)
    xTwo = logisticXarray(x2,R2,nIterations)
    for i in range (nIterations):
        xDif.append(abs(xTwo[i]-xOne[i]))

    plt.scatter(nIterationsArray,xDif)
    plt.ylabel("Trajectory Difference ( |x1-x2| )")
    plt.xlabel("Iteration Number (n)")
    plt.show()


R = 2

x1 = .2
x2 = .200001
N = 200
seePlots = False
if seePlots:
    plotLogisticDifOverIterations(x1,R,x2,R,N)
    R = 3.4
    plotLogisticDifOverIterations(x1,R,x2,R,N)
    R = 3.72
    plotLogisticDifOverIterations(x1,R,x2,R,N)

# ---- Homework 1.g ----

def avgLogisticDif(x1,R1,x2,R2,nIterations=5000):
    xOne = np.array([])
    xTwo = np.array([])
    xDif = []
    nIterationsArray = []
    for i in range (nIterations):
        nIterationsArray.append(i)

    xOne = logisticXarray(x1,R1,nIterations)
    xTwo = logisticXarray(x2,R2,nIterations)
    for i in range (nIterations):
        xDif.append(abs(xTwo[i]-xOne[i]))
    return np.average(xDif)

N = 5000
R = 3.72
print ("for n = " + str(N) + ", average difference = " + str(avgLogisticDif(x1,R,x2,R,N)) )
N = 500000
print ("for n = " + str(N) + ", average difference = " + str(avgLogisticDif(x1,R,x2,R,N)) )


# ---- Homework 2.a ----

N = 400
x = .2
R = 3.68725
if False:
    xArray = logisticXarray(x,R,N)
    nArray = []
    for i in range (N):
        nArray.append(i)
    plt.scatter(nArray,xArray)
    plt.show()

# Very beautiful, reminds me of a life lesson;
# out of a situation that seemingly never settles, 
# peace or insight is sometimes found unexpectedly


R = 3.828427124745
N = 2000000
xArray = logisticXarray(x,R,N)
nArray = []
for i in range (N):
    nArray.append(i)
plt.scatter(nArray,xArray)
plt.show()
print (xArray[-1],xArray[-2],xArray[-3])

