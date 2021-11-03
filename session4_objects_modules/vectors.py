aval=2
class vector:
    def __init__(self,x=0,y=0,z=0, desc=''):
        self.x=x
        self.y=y
        self.z=z
        self.desc=desc

    def report(self, verbose=True):
        """Returns a tuple containing the three 
            components of this vector, formatted as (x,y,z)"""
        dtag=''
        if (self.desc != ''):
            dtag='('+self.desc+')'
        if (verbose):
            print('Vector components '+dtag+': ')
            print('x: ', self.x)
            print('y: ', self.y)
            print('z: ', self.z)
        return (self.x, self.y, self.z)


def main():
    v = vector(1,2,3,desc='Sample Vector')
    v.report()

if (__name__ == "__main__"):
    main()
