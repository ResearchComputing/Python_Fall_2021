import sys
def factorial(n):
    if (n <= 1):
        return 1
    else:
        return n*factorial(n-1)

mstr = input("Enter a number: ")
m = int(mstr)
try:
    sys.setrecursionlimit(m+2)
    mfact = factorial(m)
except:
    print('You appear to be running Jupyter...')
    sys.setrecursionlimit(m+31)
    mfact = factorial(m)

print('m! is',mfact,'.')
