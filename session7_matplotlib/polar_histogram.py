###########################################################
#
#       Plotting Example
#           - displays a histogram and a polar plot
#           - provides example of Cartesian plot alongside polar plot

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


###################################################
# Give the random module a random seed (optional)
np.random.seed(19680801)

npts = 512

#Random points in theta
tmean = np.pi   # mean of distribution
tsigma = np.pi# standard  deviation of the distribution
theta = tmean+tsigma*np.random.randn(npts)   # Uniformly distributed set of points

#Random points in r
rmean = 0.0     
rsigma = 1      
r = rmean + rsigma * np.random.randn(npts)

##################################################
# Ensure that r and theta have sensible values
maxr = np.max(np.abs(r))
for i in range(npts):
    theta[i] = (theta[i] % (2*np.pi))  #*180.0/np.pi

    r[i] = np.abs(r[i])/maxr
    r[i] = r[i] % 1
    



##########################################
# Begin the figure
# Since we wish to draw a Cartesian plot
# alongside a polar plot, the sequence
# of commands we type is somewhat different
# in that figure and axes objects are initialized
# individually

# Begin by initializing the figure object
fig = plt.figure(1)

##############################
# Subplot 1 :  histogram of theta values
# Initialize our first axes object.
ax1=plt.subplot(1,2,1)  # 1 row, 2 columns, image 1  (1,2,1)

# the histogram of the data
num_bins = 50
ax1.hist(theta, num_bins, normed=1)
ax1.set_xlabel(r'$\theta$')
ax1.set_ylabel('Probability density')
ax1.set_title(r'Histogram of $\theta$-values')

################################################
# Subplot 2 : Polar Plot of our Random Points
# Initialize our second axes object and set its projection to polar

ax2=plt.subplot(1,2,2,projection='polar')  # 1 row, 2 columns, image 2 (1,2,2)

for i in range(npts):
    ax2.plot(theta[i], r[i], 'r.')   # plot each point individually (no connecting line)

ax2.set_title('Random Points')
ax2.set_rticks([0.5, 0.75, 1])  # Control radial ticks -- most easily accessible via "axes" object
ax2.set_rlabel_position(-22.5)  # Move radial labels away from plotted line

plt.tight_layout()
plt.show()
