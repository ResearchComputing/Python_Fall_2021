import h5py
import numpy as np
filename='new.hdf5'


f = h5py.File(filename,"r")

print('///////////////////////////////')
print('        File Contents          ')
def print_name(name):
    print(name)

f.visit(print_name)
#Once we know the contents, we can examine them in further detail
ds1 = f['folder1/data_range_1']
print(type(ds1))
sf1 = f['folder1/subfolder1']
print(type(sf1))



f.close()


