x = int(input('please enter a 1st positive number: '))
y = int(input('please enter a 2nd positive number: '))

# index will run from smaller to 1
# if on the way, index can be divided by both numbers
# ... then break
index = min(x, y)
while True:
    if x % index == 0 and y % index == 0:
        break
    index = index - 1
print('biggest divider', index)