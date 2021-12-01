########################################################
# Example:
#       Creating a plot with 2-D data
#       Displayed in color
#       Displayed with contours

import numpy as np
import matplotlib.pyplot as plt

#Let's create some 2-d data. 
nx = 1024
ny = 1024
mydt = 'float64'
pi = np.pi
mydata = np.zeros((nx,ny),dtype=mydt)
for i in range(nx):
    xamp = ((0.5/nx) * (nx//2-i)) **2
    for j in range(ny):
        yamp = np.cos( 2*pi*(j-ny/2)/ny)
        mydata[i,j] = xamp*yamp


################################################3
#Plot
fig, ax = plt.subplots()
# We use the pcolormesh function
img = ax.pcolormesh(mydata,cmap='jet')



###############################
# Add some contours
# Define the levels 
clevels = [-0.03, -0.02, -0.01, -0.005,  0.005, 0.01, 0.02, 0.03]
# We can also define line styles.  Make the negative levels dashed:
cstyles = ['--', '--', '--', '--', '-', '-', '-', '-' ]
cs = ax.contour(mydata, levels = clevels, linestyles=cstyles)
#If desired, we can add a colorbar
#colorbar is a method of the figure object, not the axes object
cbar = fig.colorbar(img, label='Amplitude')

ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

plt.show()
