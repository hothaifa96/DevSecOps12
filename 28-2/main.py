# while condiotion :
#     #loop

# age = 16
#
# while age < 20 :
#     print(age)
#     age += 1;
# print('after loop')

list1 = list(range(10))

# sum =0
# for i in list1 :
#     sum += i
# print(f'the sum of the list using for loop is {sum}')
#
# #---------------------
# index = 0
# sum = 0
# while index < len(list1):
#     sum += list1[index]
#     index +=1
# print(f'the sum of the list using for while is {sum}')


# write a program to receives a name from the user
# until the user enters 'guy'
# when the user input equals to guy print hello guy
# otherwise ask the user for another input

# name = input('enter a name')
# while name != 'guy':
#     print('invalid name ')
#     name = input('enter a name')
# print(f'hello {name}')

# -----------

# list4 =[1]
# for i in list4:
#     name = input('enter a name')
#     if name == 'guy':
#         break
#     else:
#         list4.append(1)

# number = int(input('enter a number : '))
# multi = 1
# while number > 0:
#     multi *= number
#     number -= 1
# print(multi)


# a valid password ends with 'omg' or starts with 'mo'
# write a program to receive a passwords from the user
# until the user insert a valid password
# print the first 2 chars of the password and 4 stars ****
#

password = input('enter a password')

while not password.endswith('omg') and \
        not password.startswith('mo') :
    password = input('invalid password, enter a password :')

print(f'{password[:2]}****')