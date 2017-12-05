class BankAccount:
    def __init__(self):
        self.balance = 0

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            raise NotEnoughMoney()
        self.balance -= amount


class NotEnoughMoney(Exception):
    pass
