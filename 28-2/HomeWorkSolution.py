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

fullname = 'Dvir Ezra'
print(fullname[-5:])  # • הדפס את חמשת התווים האחרונים במחרוזת
print(fullname[: len(fullname) // 3])  # הדפס את השליש הראשון של המחרוזת
print(fullname.count('a'))  # ספור כמה פעמים האות’ a ‘מופיעה במחרוזת
print('b' in fullname)  # כתוב פקודה הבודקת האם האות’ b ‘מופיעה במחרוזת
name_list = fullname.split()
print(name_list)
name_list.reverse()
print(name_list)
name_list[0] = name_list[0].upper()
print(name_list)

first_name = name_list[1]
half = len(first_name) // 2
name_list[1] = name_list[1][:half] + name_list[1][half + 1:]
# name_list[1] => first name Dvpr
print(name_list)

print(f'{name_list[1]} {name_list[0]}')

new_name = ' '.join(name_list)
print(new_name)
