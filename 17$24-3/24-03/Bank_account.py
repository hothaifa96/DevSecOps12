class BankAccount:
    def __init__(self, balance=0, owner='', id=0, credit_score=0):
        self.__balance = balance
        self.__owner = owner
        self.id = id
        self.__credit_score = credit_score

    def set_owner(self, new_owner):
        if isinstance(new_owner, str) and len(new_owner) > 0:
            self.__owner = new_owner

    def get_owner(self):
        return self.__owner

    def get_balance(self):
        return f'{self.__balance}$'

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def __str__(self):
        return f'bank account {self.__owner} id : {self.__credit_score}'

    def __eq__(self, other):
        return self.balance == other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __len__(self):
        return len(self.owner.split())


acc1 = BankAccount(9000, 'hodi omer rafi dvir', 4, 5)
acc2 = BankAccount(9000, 'zahi', 99, 9)
# print(acc1 == acc2)
# print(acc1 > acc2)
# print(acc1 < acc2)
# print(len(acc1))

acc1.set_owner('rafi')

print(acc1.get_balance())
