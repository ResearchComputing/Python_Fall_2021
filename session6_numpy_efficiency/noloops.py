########################################################################
#   Example:   Array syntax vs. explicit looping
#
#              Since Python is an interpretted language, explicit
#              loops are inherently slow.  It is often advantageous
#              to rewrite loops using array syntax.  This allows 
#              Python to use more efficient routines, compiled 
#              & optimized in a lower-level language (like C) where possible.
#              
#              In this example, we record the time to calculate a=a*2 and
#              c = a*b using both array syntax and explicit looping.

import numpy as np
import time

npts = 1000000
ntrials = 2
a = np.zeros(npts)
b = np.zeros(npts)


print(' ')
print('   Timing array operations vs. explicit looping')
print('   Number of elements: ', npts)
print('   Number of trials  : ', ntrials)
print(' ')

t0 = time.time()
for i in range(ntrials):
    a *= 2
t1 = time.time()
dt1 = t1-t0


t0 = time.time()
for i in range(ntrials):
    for j in range(npts):
        a[j] *= 2
t1 = time.time()
dt2 = t1-t0


t0 = time.time()
for i in range(ntrials):
    c = a*b
t1 = time.time()
dt3 = t1-t0



t0 = time.time()
for i in range(ntrials):
    for j in range(npts):
            c[j] = a[j]*b[j]
t1 = time.time()
dt4 = t1-t0

tstr1 = '{:.4e}'.format(dt1)
tstr2 = '{:.4e}'.format(dt2)
tstr3 = '{:.4e}'.format(dt3)
tstr4 = '{:.4e}'.format(dt4)

print('   In-place, Array op (a *=2)                   : '+tstr1+' seconds')
print('   In-place, explicit loop (a[j] *=2)           : '+tstr2+' seconds')
print('   Array Mult: array op ( c = a*b )             : '+tstr3+' seconds')
print('   Array Mult: explicit loop (c[j] = a[j]*b[j]) : '+tstr4+' seconds')

    


