import h5py
import numpy as np
filename='test.hdf5'


f = h5py.File(filename,"r")

integers = f['Integers']
reals = f['Reals']
print('')
print('////////////////////////////////////')
print('Integers shape: ', integers.shape)
print('Integers dtype: ', integers.dtype)
print(integers[:])

print('')
print('////////////////////////////////////')
print('Reals shape: ', reals.shape)
print('Reals dtype: ', reals.dtype)
print(reals[:,:])
print(integers.attrs['year'])
f.close()


