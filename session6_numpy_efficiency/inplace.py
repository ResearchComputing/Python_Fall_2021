###########################################################################
#   Example:  In-place vs. out-of-place operations
#           
#             We can avoid unnecessary array copying, and save time,
#             by using in-place operators where possible.
#             Use a += 2 instead of a = a+2, a *=2 instead of a = a*2, etc.

import numpy as np
import time


npts = 10000000
ntrials = 4
a = np.zeros(npts)
b = np.zeros(npts)


print(' ')
print(' Timing in-place vs. out-of-place array operations')
print(' Number of elements: ', npts)
print(' Number of trials  : ', ntrials)
print('')
# This appears to be in-place, but in fact a new array is made (a*2) and reassigned to a
t0 = time.time()
for i in range(ntrials):
    a = a*2
t1 = time.time()
dt1 = t1-t0


# This is truly in-place
t0 = time.time()
for i in range(ntrials):
    a *= 2
t1 = time.time()
dt2 = t1-t0


# And here, we have a clearly out-of-place operation (a*2 is calculated and then assigned to b)
t0 = time.time()
for i in range(ntrials):
    b = a*2
t1 = time.time()
dt3 = t1-t0

tstr1 = '{:.4e}'.format(dt1)
tstr2 = '{:.4e}'.format(dt2)
tstr3 = '{:.4e}'.format(dt3)

print('   "In-place"    ( a  = a*2 ) : '+tstr1+' seconds')
print('    In-place     ( a *= 2   ) : '+tstr2+' seconds')
print('    Out-of-place ( b  = a*2 ) : '+tstr3+' seconds')







    


