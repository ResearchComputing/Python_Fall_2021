def func1():
    global a
    a = a+1


def func2():
    b = 3
    c = 5
    def func3():
        global b
        b = b+1
        print('Value of b inside func3: ',b)   

    func3()

a=1
b=2
func1()
print('Value of a after calling func1: ', a)

func2()
print('Value of b after calling func2', b)
