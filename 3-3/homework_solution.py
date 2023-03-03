# 2
# word = 'joey doesnt share food'
#
# print(word[::-1])

# 3
# ------------ s1 ------------
# number = 100
# number_int = str(number) # '1234'
# number_int=number_int[::-1] # '4321'
# number = int(number_int)
# print(number)
# ------------ s1 ------------

# ---------- for kids ----------
# y = 0
# x = 156
# ahadot = x % 10  # 6
#
# y+=ahadot   # y= 0+6 =6
# x = x // 10 # x = 15
# ahadot = x % 10 # 5
# y*=10  # y =60
# y+=ahadot # y =65
#
# x = x // 10 #x = 1
# ahadot = x % 10 #1
# y*=10 # 650
# y+=ahadot # 651  <-> 156
# print(y)
# ---------- not for kids ----------

# origin = 1056
# result = 0
#
# while origin > 0:
#     result *= 10
#     ahadot = origin % 10
#     result += ahadot
#     origin = origin // 10
# print(result)


# ------------- 4 ---------

# for i in range(10000):
#     print(7 * i , end=' ')
#     if i == 7:
#         break

# numbers = [7 * x for x in range(10000) if x <= 7]
#
# print(numbers)


#x= [23, 4, -6, 23, -9, 21, 3, -45, -8]
# ------------ 5 -----------
# pos = []
# neg = []
#
# for n in x :
#     if n > 0:
# #         pos.append(n)
# #     else:
# #         neg.append(n)
#
# print(f'negatives : {neg}  positive : {pos}')
#------------ short answer --------
# positive = [i for i in x if i >= 0]
# negative = [i for i in x if i < 0]
#
# print(f'{positive},{negative}')

# n = []
# p = []
#
# for i in x :
#     n.append(i) if i<0 else p.append(i)
# print(f'{n}, {p}')


#--------- 7 ---------

user_input = 0
sum = 0

# while user_input != 'add':
#     user_input = float(user_input)
#     sum += user_input
#     user_input = input('enter a number :')
#
# print(sum)