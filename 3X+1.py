from random import randrange

a = 7

while a != 1:
    print(a)
    if a % 2 == 0:
        a = a // 2
    else:
        a = (a * 3) + 1

print(a)
