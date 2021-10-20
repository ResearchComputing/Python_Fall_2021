def countup_odd(n):
    """Print all odd numbers in the range [1,n] in ascending order."""
    n = int(n)  # make sure we have an integer
    if (n < 1):
        print('Error.  n must be an integer >= 1')
    if (n == 1):
        print('1')
    else:
        countup_odd(n-1)
        if (n%2 == 1):
            print(n)

def countdown_even(n):
    """Print all even numbers in the range [2,n] in descending order."""
    n = int(n)  # make sure we have an integer
    if (n < 1):
        print('Error.  n must be an integer >= 1')
    if (n == 1):
        return
    else:
        if (n%2 == 0):
            print(n)
        countdown_even(n-1)

def factorial(n):
    """Returns n!"""
    n = int(n)
    if (n <= 1):
        return 1
    else:
        return n*factorial(n-1)

def display_factorials(n):
    """Displays n! for all numbers in the range [1,n]"""
    n = int(n)
    if (n <= 1):
        print(str(n)+'! is ', 1)
    else:
        display_factorials(n-1)
        print(str(n)+'! is ', factorial(n))

n = int(input("Enter a number: "))
print(' ')
print('Displaying odd numbers in the range [1,'+str(n)+']')
countup_odd(n)

print(' ')
print('Displaying even numbers in the range [1,'+str(n)+']')
countdown_even(n)

print(' ')
print('Displaying n! for all numbers in the range [1,'+str(n)+']')
display_factorials(n)
