from homework_checker.base import Assignment

# Powerset - Napisz kod tworzęcy ze zbioru A = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# zbiór zawierający wszystkie podzbiory A (włącznie z pustym i A).
# UWAGA: w python zbiory (set) nie mogą być elementami innych zbiorów,
# proszę użyć frozenset jako zbiorów wewnętrznych.
# Wynik przypisz na zmienną result


A = frozenset((0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
answer = {frozenset()}
for x in A:
    tmp = set()
    for y in answer:
        tmp.add(y | frozenset((x,)))
    answer |= tmp


def has_full(result):
    assert A in result


def has_empty(result):
    assert frozenset() in result


def is_set(result):
    assert type(result) == set


def length_ok(result):
    assert len(result) == len(answer)


def result_ok(result):
    assert result == answer


assignment = Assignment(
    'zadanie5',
    'zadanie5.py',
    'result',
    (has_full, has_empty, is_set, length_ok, result_ok)
)
