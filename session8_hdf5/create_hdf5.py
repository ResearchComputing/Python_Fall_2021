import h5py
import numpy as np
filename='test.hdf5'

dname1="Integers"
ndata1=(100,)
dname2="Reals"
ndata2=(2,2)
f = h5py.File(filename,"w")
dset1 = f.create_dataset(dname1, ndata1, dtype='int32')
dset2 = f.create_dataset(dname2, ndata2, dtype='float64')

print('The shape of dset1 is: ', dset1.shape)
print('The type of dset1 is : ', dset1.dtype)

print('The shape of dset1 is: ', dset2.shape)
print('The type of dset1 is : ', dset2.dtype)

dset1[:] = np.arange(1,101,dtype='int32')
dset1[0] = 1000

dset2[0,:] = np.array([2.1,3.0],dtype='float64')
dset2[1,:] = np.array([55.0,-73.0001],dtype='float64')

dset1.attrs['month']=7
dset1.attrs['year']= 2017

f.close()


