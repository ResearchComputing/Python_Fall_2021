
######################################################################3
#       Example:  Timing
#
#                 Timing in Python is easily accomplished using the "time"
#                 function provided by the "time" module. A simple
#                 example is provided below.

import time
nsizes = 8

for i in range(nsizes):
    list1 = []
    list2 = []

    nelem = 10**i

    t0 = time.time()
    for j in range(nelem):
        list1.append(j)
        list2.append(i+j)
    t1 = time.time()
    dt_create = t1-t0

    t0 = time.time()
    for j in range(nelem):
        list2[j] = list2[j]*list1[j]
    t1 = time.time()
    dt_prod = t1-t0

    nestr = '{:8}'.format(nelem)
    dtcstr = '{:.4e}'.format(dt_create)
    dtpstr = '{:.4e}'.format(dt_prod)
    print('')
    print('/////////////////////////////////////////////////////////////////')
    print('  Time to create two lists of length '+nestr+' : '+dtcstr+' seconds')
    print('  Time to perform element-wise product on two lists of length '+nestr+' : '+dtpstr+' seconds')
