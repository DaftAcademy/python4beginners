import random
from unittest.mock import patch

import pytest

from zad03_bank_account_with_promo import (
    BankAccount,
    NotEnoughMoney,
)


@pytest.fixture
def bank_account():
    """
    Zwraca zainicjowany obiekt konta bankowego.
    """
    return BankAccount()


def test_bank_account_starting_amount_is_0(bank_account):
    assert bank_account.get_balance() == 0


def test_deposit_200(bank_account):
    bank_account.deposit(200)

    assert bank_account.get_balance() == 200


def test_deposit_300(bank_account):
    bank_account.deposit(300)

    assert bank_account.get_balance() == 300

def test_deposit_more_than_once(bank_account):
    bank_account.deposit(100)

    bank_account.deposit(200)

    assert bank_account.get_balance() == 300


def test_withdraw_some_money(bank_account):
    bank_account.deposit(200)

    bank_account.withdraw(100)

    assert bank_account.get_balance() == 100


def test_withdraw_some_money_2(bank_account):
    bank_account.deposit(200)

    bank_account.withdraw(50)

    assert bank_account.get_balance() == 150


def test_withdraw_when_balance_is_zero(bank_account):
    with pytest.raises(NotEnoughMoney):
        bank_account.withdraw(50)


def test_withdraw_when_not_not_enough_money_on_account(bank_account):
    bank_account.deposit(200)

    with pytest.raises(NotEnoughMoney):
        bank_account.withdraw(201)


def test_withdraw_all_money(bank_account):
    bank_account.deposit(200)

    bank_account.withdraw(200)

    assert bank_account.get_balance() == 0


def test_deposit_with_promo(bank_account):
    with patch('random.random') as mock_random:
        mock_random.return_value = 0.05
        bank_account.deposit(100, with_promo=True)

    assert bank_account.get_balance() == 101


def test_deposit_with_promo_2(bank_account):
    with patch('random.random') as mock_random:
        mock_random.return_value = 0.05
        bank_account.deposit(200, with_promo=True)

    assert bank_account.get_balance() == 201

def test_deposit_with_promo_3(bank_account):
    with patch('random.random') as mock_random:
        mock_random.return_value = 0.0999
        bank_account.deposit(300, with_promo=True)

    assert bank_account.get_balance() == 301


def test_deposit_with_promo_no_luck(bank_account):
    with patch('random.random') as mock_random:
        mock_random.return_value = 0.2
        bank_account.deposit(100, with_promo=True)

    assert bank_account.get_balance() == 100


def test_deposit_with_promo_no_luck_2(bank_account):
    with patch('random.random') as mock_random:
        mock_random.return_value = 0.1
        bank_account.deposit(100, with_promo=True)

    assert bank_account.get_balance() == 100
