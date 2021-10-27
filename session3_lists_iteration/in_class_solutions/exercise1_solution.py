def get_sum(a):
    asum = 0
    for i in a:
        asum = asum+i
    return asum

n = [1,2,3,4,5]
nsum = get_sum(n)
print("The sum of numbers 1 through 5 is: ", nsum)
