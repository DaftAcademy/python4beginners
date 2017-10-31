from homework_checker.base import Assignment

# Napisać kod tworzący listę list kolejnych elementów parzystych < 100 według
# schematu: [[0], [2], ... , [98]]. Wynikową listę przypisz na zmienną result.


def type_ok(result):
    assert type(result) == list


def length_ok(result):
    assert len(result) == 50


def second_ok(result):
    assert result[1] == [2]


def beforelast_ok(result):
    assert result[-2] == [96]


def test5(result):
    assert result == [[i] for i in range(100) if i % 2 == 0]


assignment = Assignment(
    'zadanie2',
    'zadanie2.py',
    'result',
    (type_ok, length_ok, second_ok, beforelast_ok, test5)
)
