import h5py
import numpy as np
# Open a file, add a dataset to one of the groups

f = h5py.File('new.hdf5', 'r+')
ff1 = f["folder1"]

npts = 10
ndata1 = (npts,)
dname1 = 'data_range_1'


dset1 = ff1.create_dataset(dname1, ndata1, dtype='int32')
dset1[:]=np.arange(1,npts+1,dtype='int32')
f.close()


