#   argv.py
#
#   Call syntax:
#       python {-N X -factorial -verbose}
#   Description:
#       Computes the Sum of numbers 1 through X (default) or X!.
#   Flags:
#       -verbose    :  Displays list of command line arguments passed to program
#       -factorial  :  If set, X! is computed rather than SUM[1,X]
#       -N X        :  Indicates the value of X to use (default is X=10)

def nfact(n):
    """Returns n!"""
    fact = 1
    for i in range(2,n+1):
        fact = fact*i
    return fact

def sumn(n):
    """Returns sum_1_n"""
    nsum = 0
    for i in range(1,n+1):
        nsum = nsum+i
    return nsum

def main():
    import sys

    print('')
    # The sys.argv list contains the script name along with any 
    # command-line parameters passed
    narg = len(sys.argv)

    # Scan through the argument list and
    # check for the -verbose or -v flag
    calc_fact = False
    for i in range(1,narg):
        if ( (sys.argv[i] == "-verbose") or (sys.argv[i] == '-v')):
            print('\n Command-line parameters specified for '+sys.argv[0]+':')
            print('')
            for j in range(1,narg):
                print(' ',str(j)+'.  '+sys.argv[j])
            print(' \n\n')

    # Check for -factorial flag
    calc_fact = False
    for i in range(1,narg):
        if (sys.argv[i] == "-factorial"):
            calc_fact = True
    
    # Check for a flag (-N) followed by a number.
    nval = 10
    for i in range(1,narg):
        if (sys.argv[i] == "-N"):
            try:
                nval = int(sys.argv[i+1])
            except:
                if (i+1 <= narg-1):
                    print("Error. Command-line parameter following -N could not be cast as an int.")
                    print('Specified parameter: ', sys.argv[i+1])
                else:
                    print('Error.  No value for -N was specified.')
    nstr = str(nval)
    if (calc_fact):
        factn = nfact(nval)
        fstr = str(factn)
        msg = '  '+str(nval)+'! = '+fstr
        print(msg)
    else:
        nsum = sumn(nval)
        sstr = str(nsum)
        msg = '  SUM[1,'+str(nval)+'] = '+sstr
        print(msg)
    

    print('  \n')
    


if (__name__ == '__main__'):
    main()
