n = int(input('enter num'))
while n != 0:
    while abs(n) >= 10:
        n = n // 10
    print(n)
    n = int(input('enter num'))