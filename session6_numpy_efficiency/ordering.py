##################################################################
#  Example:   Numpy array ordering
#             In this example, we demonstrate the difference between
#             row-major and column-major ordering of the array.
import numpy as np

dt    = 'int32'  # 4-byte integers

#Create a 1-D array with elements numbered 1 through 8
values = np.arange(1,9,1,dtype=dt)



#Reshape the 1-D array in two different ways

#Row-major ordering (default behavior; C-like).
#Values are loaded into row 0, then row 1, etc. 
array2d_row_major = np.reshape(values,(4,2),order='C')

#Column-major ordering (Fortran-like)
#Values are loaded into column 0, then column 1, etc.
array2d_col_major = np.reshape(values,(4,2),order='F')


print('')
print('values: ')
print(values)
print('')

print('2-D reshape; row-major):')
print(array2d_row_major)
print('')

print('')
print('2-D reshape; column-major):')
print(array2d_col_major)
print('')


