import random

class BankAccount:
    def __init__(self):
        self.balance = 0

    def get_balance(self):
        return self.balance

    def deposit(self, amount, with_promo=False):
        self.balance += amount
        if with_promo and random.random() < 0.1:
            self.balance += 1

    def withdraw(self, amount):
        if self.balance < amount:
            raise NotEnoughMoney()
        self.balance -= amount


class NotEnoughMoney(Exception):
    pass
