##################################################################
# Example:  Creating a plot with:
#  -- logarithmic axes
#  -- a legend
#  -- embedded latex formulae
# To begin with, we import the pyplot package from matplotlib
# Common practice is to alias pyplot as plt
# We also import numpy

import matplotlib.pyplot as plt
import numpy as np

###############################################
# Let's generate some sample data to plot
# We will plot two functions of x
pi = np.pi
npts = 64
mydt='float64'
x  = np.linspace(0.1,10,npts,dtype=mydt)

y1 = x
y2 = x*x
y3 = x*x*x
###############################################

# To create a legend, we use the label 
# keyword when creating each of our plots
# If we wish, we can use latex by setting label=r'$latex formula$' .
# Note that the 'r' goes outside the quotes.


fig, ax = plt.subplots()
ax.plot(x,y1,label = 'x')
ax.plot(x,y2,'go',label = r'$x^2$'+' (with latex)') # green circles (first letter g = green; second letter o = filled circle)
ax.plot(x,y3,'r--',label=r'$x^3$'+' (with latex)')  # red dashed lines (first letter r = red; second characters indicate line pattern)

ax.set_xlabel('Logarithmic x-axis')
ax.set_ylabel('Logarithmic y-axis')
ax.set_title('Plot Title')

# To use logarithmic axes, call the set_xscale and set_yscale methods and pass the value "log."
ax.set_yscale('log')
ax.set_xscale('log')

# Once our plot is set, call the legend function 
# loc controls the placement relative to the ax bounds.
# ncol controls the number of columns used in the legend.
legend = plt.legend(loc='lower right', shadow=True, ncol = 2) 

plt.show()



