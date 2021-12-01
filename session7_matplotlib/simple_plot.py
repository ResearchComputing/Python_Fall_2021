############s######################################################
# Example:  Creating a line plot
# To begin with, we import the pyplot package from matplotlib
# Common practice is to alias pyplot as plt
# We also import numpy

import matplotlib.pyplot as plt
import numpy

###############################################
# Let's generate some sample data to plot
# We will plot two functions of x
pi = numpy.pi
npts = 64
mydt='float64'
x  = numpy.linspace(0,2*pi,npts,dtype=mydt)

y1 = x
y2 = x*x
y3 = numpy.cos(2*x)
###############################################

# We will display the figure on the screen by default.
# Set this to "True" in order to save the figure to the disk.
savefig=False

# Set the dimensions   
width_inches  = 8
height_inches = 4
sizetuple=(width_inches,height_inches)

# Initialize a figure and an axes object.
# The Figure instance is a container for multiple
# plots (axes objects).  We mainly work with axes
# objects.

fig, ax = plt.subplots(figsize=sizetuple)


ax.plot(x,y1)        # Plot our first curve

# Matplotlib choose default colors based on the ordering of the plots.
# The first plot is blue, the second is orange, etc.
# We can control the color using a single-character string corresponding
# to the first letter of the color we want to use.

# We can also add additional characters that indicate the linestyle we would like to adopt.
# For other available symboles and linestyles, see 
#  https://matplotlib.org/api/markers_api.html

ax.plot(x,y2,'go')   # green circles (first letter g = green; second letter o = filled circle)
ax.plot(x,y3,'r--')  # red dashed lines (first letter r = red; second characters indicate line pattern)

# The set_{xlabel, ylabel, title} functions control the axis labels and plot title
ax.set_xlabel('x-axis label')
ax.set_ylabel('y-axis label')
ax.set_title('Plot Title')

# Calling the tight_layout() function ensures that margins
# for the current figure are set so that axis labels, titles, etc.
# all fit nicely on the page.
plt.tight_layout() 

# Finally, we display our figure to the screen or save it to disk.
if (savefig):
    # Python can save figures in a variety of formats.
    #ext='png'
    #ext='jpeg'
    ext='pdf'
    filename = 'simple_plot.'+ext
    plt.savefig(filename)
else:
    #To view the plot on our screen, we use the "show" function.
    plt.show()



