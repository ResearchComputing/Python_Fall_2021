import h5py
import numpy as np
# Open a file, add a dataset to one of the groups

f = h5py.File('new.hdf5', 'r+')
ff1 = f["folder1"]
fsub = ff1.create_group("subfolder1")

npts = 10
ndata2 = (npts,)
dname2 = 'data_set_2'


dset2 = fsub.create_dataset(dname2, ndata2, dtype='int32')
dset2[:]=np.arange(21,31,dtype='int32')

ff2 = f["folder2"]
fsub2 = ff2.create_group("subfolder2/subfolder3/subfolder4")
f.close()


