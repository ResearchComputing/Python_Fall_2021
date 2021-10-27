def collatz_sequence(n):
    if (n <= 1):
        return [1]
    num = n
    seq = [n]
    while (num > 1):
        num_mod = num%2
        if (num_mod == 0):
            num = num//2
        else:
            num = 3*num+1
        seq.append(num)
    return seq

mstr = input("Enter a positive integer: ")
mseq = collatz_sequence(int(mstr))
print("The Collatz sequence for "+mstr+" is: ")
print(mseq)
