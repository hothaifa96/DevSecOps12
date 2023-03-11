
x = int(input('enter a number for prime detection'))
i = 2
while x % i != 0:
    i += 1
if i == x:
    print('prime')
else:
    print('not prime')
