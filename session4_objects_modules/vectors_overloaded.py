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

    def mag(self):
        """ Returns the amplitude of this vector."""
        vmag = (self.x**2+self.y**2+self.z**2)**(0.5)
        return vmag

    def __add__(self,other):
        """Returns the sum of self and other."""
        xnew = self.x+other.x
        ynew = self.y+other.y
        znew = self.z+other.z
        return vector(xnew, ynew, znew)

    def __sub__(self,other):
        """Returns the difference of self and other."""
        xnew = self.x-other.x
        ynew = self.y-other.y
        znew = self.z-other.z
        return vector(xnew, ynew, znew)

    def __mul__(self,other):
        """ Returns the dot-product of self and other."""
        dprod= self.x*other.x+self.y*other.y+self.z*other.z
        return dprod

    def __pow__(self,other):
        """Returns the difference of self and other."""
        xnew = self.y*other.z-self.z*other.y
        ynew = self.z*other.x-self.x*other.z
        znew = self.x*other.y-self.y*other.x
        return vector(xnew, ynew, znew)

def main():
    v = vector(1,2,3,desc='Vector "v"')
    w = vector(4,5,6,desc='Vector "w"')
    v.report()
    w.report()
    print('The magnitude of "v" is: ', v.mag())
    print('The magnitude of "w" is: ', w.mag())
    sum_vw = v + w
    print('Their sum is: ', sum_vw.report(verbose=False))
    diff_vw = v - w
    print('Their difference is: ', diff_vw.report(verbose=False))
    print('Their dot product is: ', v*w)
    cross_vw = v**w
    cross_wv = w**v
    print('v x w is : ', cross_vw.report(verbose=False))
    print('w x v is : ', cross_wv.report(verbose=False))

if (__name__ == "__main__"):
    main()
