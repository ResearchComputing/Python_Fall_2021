def grade(a):
    if (a >= 90):
        return 'A'
    elif (a >= 80):
        return 'B'
    elif (a >= 70):
        return 'C'
    elif (a >= 60):
        return 'D'
    else:
        return 'F'

print(grade(50))
print(grade(61))
print(grade(72))
print(grade(85))
print(grade(92))
