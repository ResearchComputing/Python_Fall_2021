for i in range(1,260):
    print(i, id(i)-id(i-1))
print(' ')
for i in range(260,0,-1):
    print(i, id(i)-id(i-1))
