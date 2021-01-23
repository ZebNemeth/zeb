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


# ---- Question 1 ----

R = 2.5
x = 0.5
print ( logisticFunction( logisticFunction( logisticFunction( logisticFunction( x, R ), R ), R ), R ) )
print ( logisticFunction( logisticFunction( logisticFunction( x, R ), R ), R ) ) # Answer
print ( logisticFunction( logisticFunction( x, R ), R ) )
print ( logisticFunction( x, R ) )
print ( x, R )
print ( logisticIterator( x, R ) )

# ---- Question 2 ----
print ( logistic( 0.5, 2.5, 3 ) ) #check
print ( logistic( 0.2, 2.6, 10 ) )

