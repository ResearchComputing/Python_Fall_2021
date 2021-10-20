import sys
def factorial(n):
    if (n <= 1):
        return 1
    else:
        return n*factorial(n-1)

mstr = input("Enter a number: ")
m = int(mstr)
sys.setrecursionlimit(m+2)

print('m! is',factorial(m),'.')
