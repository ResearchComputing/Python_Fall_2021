##########################################################################
#       Example:  Map & Reduction in Serial Python
#               
#                 If we have a function designed to accept one argument,
#                 but want to evaluate it for multiple data values, we
#                 can use Python's "map" function as shorthand for a loop.
#
#                 If we have a function that we would like to call again
#                 and again, using results from one call in tandem with
#                 the subsequent call, we can use "reduce" function.
#
#                 The following program demonstrates the use of map & reduce.
from functools import reduce
def squarex(x):
    return (x*x)
def add(x):
    return (x+x)

def addtwo(x,y):
    return x+y
def multtwo(x,y):
    return x*y

arg_list = [1,3,9,27]
# Compute the square of 1,3,9, and 27
vals = map(squarex, [1,3,9,27])

for i,v in enumerate(vals):
    str1 = '{:2d}'.format(arg_list[i])
    str2 = '{:3d}'.format(v)
    print(str1+' squared is '+str2+'.')


#Compute ((1+2)+3)
#   -- first 1 and 2 are passed to addtwo
#   -- next, (1+2 = 3) and 3 are passed to addtwo
#   -- the final result is assigned to v2
res1 = reduce(addtwo,[1,2,3])

#Compute (((1*2) * 3) * 4)
#   -- first 1 and 2 are passed to multtwo
#   -- next, (1*2=2) and 3 are passed to addtwo
#   -- next (2*3=6)  and 4 are passed to addtwo 
#   --  the final result is assigned to res2
res2 = reduce(multtwo,[1,2,3,4])
print('')
print('  1+2+3 = ', res1)
print('1*2*3*4 = ', res2)

