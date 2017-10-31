from homework_checker.base import Assignment

# Stwórz listę 100 list, każda z liczbami od 1 do 100. Potem dla każdej j-tej
# z tych list wewnętrznych na jej końcu dodać sumę jej pierwszych elementów
# do j-tego włącznie.
# Spodziewany efekt: [ [1, 2, 3, ..., 100, 1], [1, 2, 3, ..., 100, 3],
# [1, 2, 3, ..., 100, 6], ..., [1, 2, 3, ..., 100, 5050] ]
# Wynikową listę przypisz na zmienną result


def test1(result):
    assert type(result) == list


def length_ok(result):
    assert len(result) == 100


def first_ok(result):
    expected_result = list(range(1, 101)) + [1]
    assert result[0] == expected_result


def last_ok(result):
    expected_result = list(range(1, 101)) + [5050]
    assert result[-1] == expected_result


def result_ok(result):
    sum_list = [list(range(1,101)) for x in range(100)]
    i = 0
    while i < 100:
        sum_list[i].append(sum(sum_list[i][:i + 1]))
        i += 1
    assert result == sum_list


assignment = Assignment(
    'zadanie3',
    'zadanie3.py',
    'result',
    (test1, length_ok, first_ok, last_ok, result_ok)
)
