import numpy as np
#Write the number 769 out to disk in native Endianness
my_number = np.zeros(1,dtype='int16')
my_number[0]=769
my_number.tofile('769.dat')

