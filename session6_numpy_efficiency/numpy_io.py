##################################################################################
#  Example:   Writing & reading numpy arrays
#
#             We can write array contents in unformatted binary using tofile.
#             We can read from a file using fromfile.
#
#             NOTE:   Regardless of an array's ordering, tofile will
#                     ALWAYS write the array in row-major order.
#                     To see this, change the ordering of simple_array to 'F.'
#                     array2d[a,b] and array3d will remain unchanged.

import numpy as np

ofile = 'numpy_output.dat'
dt    = 'int32'  # 4-byte integers


simple_array = np.zeros((4,2),dtype=dt)

simple_array[0,0] = 1
simple_array[0,1] = 2
simple_array[1,0] = 3
simple_array[1,1] = 4
simple_array[2,0] = 5
simple_array[2,1] = 6
simple_array[3,0] = 7
simple_array[3,1] = 8

#Writing an array is easy - just specify a filename
simple_array.tofile(ofile)

#When reading unformatted binary, we specify 
#   (1)  The filename
#   (2)  The datatype
#   (3)  The number of values to read

values = np.fromfile(ofile,dtype=dt,count=8)

#We can reshape the data as desired
array2da = np.reshape(values,(4,2))
array2db = np.reshape(values,(2,4))
array3d = np.reshape(values,(2,2,2))

print('')
print('values: ')
print(values)
print('')

print('2-D array; 4 rows, 2 columns):')
print(array2da)
print('')

print('')
print('2-D array; 2 rows, 4 columns):')
print(array2db)
print('')

print('')
print('3-D array:')
print(array3d)
print('')
