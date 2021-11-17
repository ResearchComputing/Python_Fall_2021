#//////////////////////////////////////////////////////////////
#                   Exercise 1:
# Rewrite the following program using numpy arrays and 
# array operations where possible (instead of explicit loops).
import numpy as np
n = 1000000  

# We can use the arange function to initialize an array with integer spacing
# between adjacent values.
istart = 1
iend = n
iskip = 1
inds = np.arange(istart,iend+1,iskip,dtype='float32')

# We use array syntax for calculating a and b
a = 4*inds
b = inds*inds

# We can perform the sum efficiently using numpy's sum function
dsum = np.sum(a*b)


print 'dsum is: ', dsum
