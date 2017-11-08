from homework_checker.base import Assignment


# Zadanie 1
# Napisz funkcję power, która dla danego n i p zwraca w wyniku n podniesione do potęgi p.
# Domyślna wartość argumentu p to 2.
# Niech n i p będą liczbami całkowitymi >= 0.


def power(n, p=2):
    return n ** p


# testy poprawnosci


def power_5_3(func):
    """Czy podniesienie 5 do 3 potęgi zwraca 125?"""
    assert func(5, 3) == 125


def default_arg_2(func):
    """Czy drugi argument ma domyślną wartość 2?"""
    assert func(5) == 25


def p_zero(func):
    """Czy podniesienie do potęgi zerowej zwraca poprawny wynik (1)?"""
    assert func(5, 0) == 1


def n_zero(func):
    """Czy podnoszenie zera do potęgi działa poprawnie?"""
    assert func(0, 5) == 0


assignment = Assignment(
    'zadanie1',
    'zadanie1.py',
    'power',
    (power_5_3, default_arg_2, p_zero, n_zero)
)
