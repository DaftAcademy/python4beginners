from homework_checker.base import Assignment


# Zadanie 2
# Napisz funkcję copy_reversed, która przyjmuje dwie listy, list_a i list_b
# i która dodaje do listy list_b całą zawartość list_a, ale w odwróconej kolejności.
# Funkcja copy_reversed niech zwraca None.



def copy_reversed(list_a, list_b):
    list_b.extend(reversed(list_a))


# test poprawnosci

def return_none(func):
    """Czy funkcja zwraca pusty wynik (None) wg treści zadania?"""
    assert func([1, 2, 3], [4, 5, 6]) is None


def list_b_changed(func):
    """Czy lista podana jako drugi argument sie zmieniła? (czytanie treści zadania)"""
    x = [1, 2, 3]
    y = [4, 5, 6]
    func(x, y)
    assert y == [4, 5, 6, 3, 2, 1]


def list_a_not_changed(func):
    """Czy lista podana jako pierwszy argument zmieniła sie w trakcie zamiast zostać skopiowana?"""
    x = [1, 2, 3]
    y = [4, 5, 6]
    func(x, y)
    assert x == [1, 2, 3]


def list_a_empty(func):
    """Czy działa dla pustej listy w pierwszym argumencie?"""
    x = []
    y = [4, 5, 6]
    func(x, y)
    assert y == [4, 5, 6]


assignment = Assignment(
    'zadanie2',
    'zadanie2.py',
    'copy_reversed',
    (return_none, list_b_changed, list_a_not_changed, list_a_empty)
)
