##################################################################
# Example:  Creating two figures in the same window
# This works largely like before, just create a second figure. before calling plt.show().
# Useful for interactive work; not so useful for saving figures (use subplots for that).

import matplotlib.pyplot as plt
import numpy as np

###############################################
# Let's generate some sample data to plot
# We will plot two functions of x
pi = np.pi
npts = 64
mydt='float64'
x  = np.linspace(0,2*pi,npts,dtype=mydt)

y1 = x
y2 = x*x
y3 = np.cos(2*x)
###############################################

# Figure 1
fig1, ax1 = plt.subplots()
ax1.plot(x,y1)
ax1.plot(x,y2,'go')   # green circles (first letter g = green; second letter o = filled circle)
ax1.plot(x,y3,'r--')  # red dashed lines (first letter r = red; second characters indicate line pattern)
ax1.set_xlabel('x-axis')
ax1.set_ylabel('y-axis')
ax1.set_title('Plot Title')


# Figure 2
fig2, ax2 = plt.subplots()
ax2.plot(x,y1,'r.')   # Simple line plot
ax2.plot(x,y2,'g-')   # plot
ax2.plot(x,y3,'b')
ax2.set_xlabel('x-axis')
ax2.set_ylabel('y-axis')
ax2.set_title('Plot Title2')

# Display both figures
plt.show()
