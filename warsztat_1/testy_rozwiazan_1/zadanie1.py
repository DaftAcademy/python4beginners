from homework_checker.base import Assignment


# Stwórz listę liczb od 0 do 999.
# Liczby podzielne przez 3 zastąp słowem 'trzy'.
# Liczby podzielne przez 5 zastąp słowem 'pięć'.
# Liczby podzielne jednocześnie przez 3 i 5 zastąp słowem 'trzypięć'.
# Wynikową listę przypisz zmiennej result.


def fifteen_ok(result):
    assert result[15] == 'trzypięć'


def three_ok(result):
    assert result[3] == 'trzy'


def four_ok(result):
    assert result[4] == 4


def five_ok(result):
    assert result[5] == 'pięć'


def result_ok(result):
    expected_list = []
    for i in range(1000):
        if i % 3 == 0 and i % 5 == 0:
            expected_list.append('trzypięć')
        elif i % 3 == 0:
            expected_list.append('trzy')
        elif i % 5 == 0:
            expected_list.append('pięć')
        else:
            expected_list.append(i)
    assert result == expected_list


assignment = Assignment(
    'zadanie1',
    'zadanie1.py',
    'result',
    (fifteen_ok, three_ok, four_ok, five_ok, result_ok)
)
