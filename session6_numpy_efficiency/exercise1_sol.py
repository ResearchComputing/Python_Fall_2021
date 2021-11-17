#//////////////////////////////////////////////////////////////
#                   Exercise 1:
# Rewrite the following program using numpy arrays and 
# array operations where possible (instead of explicit loops).
import time
import numpy
n = 1000000  

t1 = time.time()
ai = numpy.arange(1,n+1,1,dtype='float64')
a = 4*ai
b = ai*ai

t2 = time.time()
dt1 = t2-t1

t1 = time.time()
dsum = 0.0
#c= a*b
#dsum = numpy.sum(c)
dsum=numpy.dot(a,b)
t2 = time.time()
dt = t2-t1


print('init time: ', dt1)
print('calc time: ', dt)
print('dsum is: ', dsum)
