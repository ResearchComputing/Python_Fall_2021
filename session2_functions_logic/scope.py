def function1():
    a = 1
    b = 3
    print(' function1: ', 'a =  ', a, 'b = ', b, 'c = ', c)
    function2()
    
def function2():
    a = -1
    print(' function2: ', 'a = ', a, 'b = ', b, 'c = ', c)

def function3():
    def function2():
        a = -1
        print('function2a: ', 'a = ', a, 'b = ', b, 'c = ', c)
    a = 1
    b = 3
    function2()



c=7
a=5
b=6
#The print statement below sees the values of a,b,c defined in the main program.
print('      main: ', 'a =  ', a, 'b = ', b, 'c = ', c)

#Function1 contains a local definition of a, and b
#...function1 retrieves the value of c from the main program, where it was defined
#Function2 is called from within function1.  Function2 contains a local definition of a.
#...function2 retrieves the values of b and c from the main program, where it was defined.
function1()

#When function3 is called, it defines values for a and b.
#Function3 calls its own version of function2, which defines the value for a.
#...function2a retrieves its value of b from function3, where it was defined.
#...function2a retreives its value of c from the main program, where function3 was defined. 
function3()

