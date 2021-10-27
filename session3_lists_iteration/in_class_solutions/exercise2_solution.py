def gen_odds(n):
    a = []
    for i in range(n+1):
        if (i%2 == 1):
            a.append(i)
    return a


num = int(input("Enter a number: "))
odds = gen_odds(num)
print(odds)
