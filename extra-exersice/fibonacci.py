a = 1
b = 1
i = int(input('enter fibonacci index'))

if i == 1 or i == 2:
    print(1)
else:
    current = 2
    while current < i:
        c = a + b
        a = b
        b = c
        current += 1
    print(c)