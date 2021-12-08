import h5py
import numpy as np
f = h5py.File('new.hdf5', 'w')
ff1 = f.create_group("folder1")
ff2 = f.create_group("folder2")
f.close()
