# class Car:
#     def __init__(self, make, model, topspeed=00):
#         self.make = make
#         self.model = model
#         self.topspeed = topspeed
#
#     def __str__(self):
#         return f'{self.make} -> {self.topspeed}'
#
#     def __repr__(self):
#         return f'Car(\'{self.make}\', \'{self.model}\', {self.topspeed})'
#
#
# audi = Car('audi', 'A8', 250)
#
# print(audi.__repr__())
#


# hm -1

# class BankAccount:
#     def __init__(self, first_name, last_name, account_id, balance):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.account_id = account_id
#         self.__balance = balance
#
#     def get_balance(self, country):
#         country = country.lower()
#         rate = 1 if country == 'israel' else 3.7 if country == 'usa' else 3.88 if country =='france' else 4.37
#         # if country == 'israel':
#         #     rate = 1
#         # elif country=='usa':
#         #     rate = 3.7
#         # else:
#         #     rate= 3.88
#         return self.__balance / rate
#
#     def __eq__(self, other):
#         return self.__balance == other.__balance
#
#     def __gt__(self, other):
#         return self.__balance > other.__balance
#
#     def __add__(self, other):
#         return self.__balance + other.__balance
#
#
# acc1 = BankAccount('omer', 'ssh', 12344, 99000)
# acc2 = BankAccount('tzahi', 'ssh', 9999, 25)
#
# print('= eq', acc1 == acc2)
# print('> gt ', acc1 > acc2)
# print('> gt ', acc1 < acc2)
# print(acc1 + acc2)
#
# print(acc1.get_balance('USA'))

# class Student:
#     def __init__(self, name, age, subj, grade):
#         self.name = name
#         self.age = age
#         self.subj = subj
#         self.__grade = grade
#
#     @property
#     def grade(self):
#         if 90 < self.__grade <= 100:
#             return 'A'
#         elif 80 < self.__grade <= 90:
#             return 'B'
#         elif 70 < self.__grade <= 80:
#             return 'C'
#         else:
#             return 'F'
#
#     @grade.setter
#     def grade(self, new_grade):
#         self.__grade = new_grade
#
#
# s1 = Student('dvir', 29, 'devops', 92)
#
# print(s1.grade)