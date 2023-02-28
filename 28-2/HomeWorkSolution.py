# for d in [1, 23, 4, 5, 6, 7]:
#     # code Block
#     print(d,end=' ')

# 3
# numbers = [100, 8, 7, 5, 1]
#
# half_numbers = len(numbers) // 2  # 5 //2 == 2
#
# for i in range(half_numbers + 1):
#     print(numbers[i])

# 4
# words = ['coding of world', 'pen', 'python', 'hello']
#
# for i in  words:
#     print(i.upper())

# 5
# words = ['coding of world','hothaifa', 'pen', 'python', 'hello']
#
# for i in words:
#     if len(i) < 4:
#         break
#     print(i.upper())

# names = ['hothaifa','zoubi','from','naura']
# for name in names:
#     for letter in name:
#         print(letter)
#     print(name)
# 6

# fullname = 'Dvir Ezra'
# print(fullname[-5:])  # • הדפס את חמשת התווים האחרונים במחרוזת
# print(fullname[: len(fullname) // 3])  # הדפס את השליש הראשון של המחרוזת
# print(fullname.count('a'))  # ספור כמה פעמים האות’ a ‘מופיעה במחרוזת
# print('b' in fullname)  # כתוב פקודה הבודקת האם האות’ b ‘מופיעה במחרוזת
# name_list = fullname.split()
# print(name_list)
# name_list.reverse()
# print(name_list)
# name_list[0] = name_list[0].upper()
# print(name_list)
#
# first_name = name_list[1]
# half = len(first_name) // 2
# name_list[1] = name_list[1][:half] + name_list[1][half + 1:]
# # name_list[1] => first name Dvpr
# print(name_list)
#
# print(f'{name_list[1]} {name_list[0]}')
#
# new_name = ' '.join(name_list)
# print(new_name)

# 7
# word = 'hello world!'
#
# print(word.find('o')) # index of first o
# print(word.rfind('o')) # index of last o
# print(word[:word.index('o')])
# print(word[word.rfind('o'):])
# 8

# print(word)
# print(word.replace('o',''))


# 9

# list1 = [8, 1000, -3, 2, 5]
#
# # sum = 0
# #
# # for i in list1:
# #     sum += i
# # print(sum)
#
# # max = list1[0]
# #
# # for i in list1:
# #     if i > max:
# #         max = i
# # print(max)
# print(max(list1))
# print(min(list1))
# sum = 0
#
# for i in list1:
#     sum += i
#
# avg = sum//len(list1)
# print(f'sum is : {sum}\nand the average is : {avg}')
#
# list1.remove(len(list1)//2)
# print(list1)
#
# list1.sort()
# print(list1)
#
# for i in range(5):
#     print(list1)
#
# list1.remove(list1[0])
# print(list1)
#
# list2 = []
# for i in list1:
#     if i < avg:
#         list2.append(i)
#
# print(list2)
#
# numbers = [1, 5, 7, 8, 100]
#
# max = numbers[0]
#
# for number in numbers:
#     if number > max:
#         max = number
# print(max)


matrix = [[4, 8, 200],
          [4, 3000, -1],
          [5, 87, 12]]

min = matrix[0][0]
for row in matrix:
    for number in row:
        if number < min:
            min = number
print(min)
