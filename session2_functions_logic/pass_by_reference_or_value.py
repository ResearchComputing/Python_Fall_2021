class MyClass:
    def __init__(self):
        self.val=1
    def setval(self,newval):
        self.val=newval
    def printval(self):
        print("My value is: ", self.val)

def modobj1(obj):
    """Side effect: alters the value of obj.val"""
    obj.val=3
def modobj2(obj):
    """Side effect: alters the value of obj.val"""
    obj.setval(4)
def modscalar(a):
    """No side effects. Only the local value of a is altered."""
    a=2
def modlist(a):
    """Side effect: alters the value of a[0]"""
    a[0]=1

print("/////////////////////////////////////////////")
print(" ")
print("Scalar datatypes behave as though passed by value.")
print(" ")
a=1
print("The value of 'a' is :", a)
modscalar(a)
print("The value of 'a' is now: ", a)
print(" ")
a=10.2
print("The value of 'a' is :", a)
modscalar(a)
print("The value of 'a' is now: ", a)
print(" ")

print("/////////////////////////////////////////////")
print(" ")
print("Entire lists are passed by reference.")
a=[5, 7]
print("The value of 'a' is :", a)
modlist(a)
print("The value of 'a' is now: ", a)

print(" ")
print("Sub-lists behave as though passed by value.")
modscalar(a[1])
print("The value of 'a' is now: ", a)
print(" ")

print("/////////////////////////////////////////////")
print(" ")
print("Objects are passed by reference.")
myobj=MyClass()

myobj.printval()
modobj1(myobj)
myobj.printval()

modobj2(myobj)
myobj.printval()
