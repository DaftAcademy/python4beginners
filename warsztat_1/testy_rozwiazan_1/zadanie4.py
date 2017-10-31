from homework_checker.base import Assignment

# Napisz kod transformujący podany słownik:
# {
#     1: 'Poniedziałek',
#     2: 'Wtorek',
#     3: 'Środa',
#     4: 'Czwartek',
#     5: 'Piątek',
#     6: 'Sobota',
#     7: 'Niedziela'
# }
# do postaci:
# {
#     'Poniedziałek': 1,
#     'Środa': 3,
#     'Piątek': 5,
#     'Niedziela': 7
# }
# (Zamiana klucza z wartością i zostawienie tylko dni nieparzystych).
# Wynik przypisz na zmienną result


def length_ok(result):
    assert len(result) == 4


def types_ok(result):
    for k in result.keys():
        assert type(k) == str


def has_poniedzialek(result):
    assert 'Poniedziałek' in result


def result_ok(result):
    expected_result = {
        'Poniedziałek': 1,
        'Środa': 3,
        'Piątek': 5,
        'Niedziela': 7
    }
    assert result == expected_result


assignment = Assignment(
    'zadanie4',
    'zadanie4.py',
    'result',
    (length_ok, types_ok, has_poniedzialek, result_ok)
)
