def dotprod(a,b):
    alen = len(a)
    blen = len(b)
    if (alen != blen):
        return
    
    j = 0
    my_sum = 0
    while (j < alen):
        prod = a[j]*b[j]
        my_sum+=prod
        b[j]=prod
        j=j+1
    return my_sum

### Test code

#First, check lists of different length -- should get 'None'
c = [1,2,3]
d = [1,4]
e = dotprod(c,d)
print('e is: ', e)
print('')

#Next, check the dot product
c = [1,2,3]
d = [4,5,6]
e = dotprod(c,d)
print('e is: ', e) # Should be 32 (4 + 10 + 18)
for j in range(len(d)):
    dstr = 'd['+str(j)+'] is now: '+str(d[j])
    print(dstr)


