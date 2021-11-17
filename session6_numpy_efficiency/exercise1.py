#//////////////////////////////////////////////////////////////
#                   Exercise 1:
# Rewrite the following program using numpy arrays and 
# array operations where possible (instead of explicit loops).
import time
n = 1000000  

t1 = time.time()
a = []
b = []
for i in range(1,n+1):
    a.append(4*i)
    b.append(i**2)
t2 = time.time()
dt1 = t2-t1

t1 = time.time()
dsum = 0.0
for i in range(n):
    dsum += a[i]*b[i]
t2 = time.time()
dt = t2-t1
print('init time: ', dt1)
print('calc time: ', dt)
print('dsum is: ', dsum)
