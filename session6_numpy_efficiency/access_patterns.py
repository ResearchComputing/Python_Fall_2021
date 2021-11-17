####################################################################
# Example:    Numpy array access patterns
#
#             In general, try not to loop over array elements; use
#             vectorized operations whenever possible.  That said,
#             sometimes loops cannot be avoided.  When you HAVE to write a 
#             loop, the order in which you access the array can affect 
#             computation speed.  If the array is row-major (default), 
#             it is most efficient to work row-by-row.  If the array is 
#             column major, work column-by-column instead.
#
#             In this example, we perform vector dot products with
#             rows and columns of an arrays that are both row-major
#             and column-major

from time import time
import numpy as np


nx = 64
nsizes = 6
ntests = 50
orders = ['C', 'F']
otitles = [' Row Major (C-style)', 'Column Major (Fortran-style)']
print('Vector-Matrix Multiplication Timings')

for i,o in enumerate(orders):
    print(' ')
    print('Array ordering: ', otitles[i])
    for k in range(nsizes):
        nxy = nx*(2**k)
        nxys = 'nx: '+'{:4}'.format(nxy)
        
        vec = np.zeros(nxy,dtype='float64', order=o)
        mat = np.zeros((nxy,nxy),dtype='float64', order=o)

        # first pass:  vec = mat[:,j]
        t0 = time()  
        for n in range(ntests):
            for j in range(nxy):
                vec2 = mat[:,j]
                dsum = np.sum(vec2*vec)
            t1 = time()
        dt1 = (t1-t0)/ntests

        # second pass:  vec = mat[j,:]
        t0 = time()  
        for n in range(ntests):
            for j in range(nxy):
                vec2 = mat[j,:]
                dsum = np.sum(vec2*vec)
            t1 = time()

        dt2 = (t1-t0)/ntests
        s2 = 1.0/dt2
        s1 = 1.0/dt1
        ds = (s2-s1)/s1
        ds = ds*100
        dratio = dt1/dt2
        dss = '{:.4f}'.format(dratio)
        dss = '(Column-wise Time)/(Row-wise time) = '+dss
        print(nxys, ';', dss)
