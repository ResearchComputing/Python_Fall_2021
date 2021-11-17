###############################################################################
#   Example:   Using Numpy arrays instead lists
#
#              Using numpy array syntax can speed up a calculation considerably.
#              We illustrate this by recording the time needed to perform
#              a = a*2 and c = a*b for lists and Numpy arrays with large
#              element counts.

import numpy as np
import time

npts = 10000000    # number of elements in each list/array
ntrials = 2        # number of times to repeat the calculation

#Initialize our Numpy arrays
a = np.zeros(npts)
b = np.zeros(npts)

#Initialize our lists
d = []
e = []
f = []
for i in range(npts):
    d.append(0.1)
    e.append(2.0)
    f.append(0.0)

print(' ')
print('Timing array vs. list operations for arrays having '+str(npts)+' elements...')

t0 = time.time()
a = a*2
t1 = time.time()
dt1 = t1-t0


t0 = time.time()
c = a*b
t1 = time.time()
dt2 = t1-t0

tstr = '{:.4e}'.format(dt1)
tstr2 = '{:.4e}'.format(dt2)
print('')
print('Time to compute a=a*2 using numpy array syntax: '+tstr+' seconds')
print('Time to compute c=a*b using numpy array syntax: '+tstr2+' seconds')


t0 = time.time()
for j in range(npts):
    d[j] = d[j]*2
t1 = time.time()
dt3 = t1-t0

t0 = time.time()
for j in range(npts):
    f[j] = d[j]*e[j]
t1 = time.time()
dt4 = t1-t0

tstr3 = '{:.4e}'.format(dt3)
tstr4 = '{:.4e}'.format(dt4)
print('')
print('Time to compute a=a*2 using lists: '+tstr3+' seconds')
print('Time to compute c=a*b using lists: '+tstr4+' seconds')


