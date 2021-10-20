
def factorial(n):
    if (n <= 1):
        return 1
    else:
        return n*factorial(n-1)

mstr = input("Enter a number: ")
m = int(mstr)
try:
    print(str(m)+'! is ',factorial(m),'.', sep='')
except:
    print('An error occurred.  Program will continue')

print("Program complete!")
