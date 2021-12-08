import h5py
import numpy as np

f = h5py.File('new.hdf5', 'w')

f1 = f.create_group("folder1")
f2 = f.create_group("folder2")

ndata = (10,)
dname2 = 'data_set_2'
dset2 = f1.create_dataset(dname2, ndata, dtype='int32')

f1sub1 = f1.create_group("subfolder1")

f.close
