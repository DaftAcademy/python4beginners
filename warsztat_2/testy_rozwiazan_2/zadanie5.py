from homework_checker.base import Assignment


# Zadanie 5
# Napisz funkcję function_results_sum, która przyjmuje dowolną liczbę funkcji
# jako argumenty pozycyjne.
# Argumenty do poszczególnych funkcji przekazywane są do function_results_sum jako keyword arguments w
# postaci NAZWA_FUNKCJI=ARGUMENTY.
# Funkcja function_results_sum powinna zwrócić sumę wyników otrzymanych
# po odpaleniu każdej z funkcji z odpowiednimi argumentami.
# Jeżeli funkcja jest bezargumentowa, nie oczekuje się podania do niej
# argumentów
# Gdy funkcja przyjmuje jeden argument, jako keyword argument przekazany
# będzie int, np. one_arg_function_name=2
# Gdy funkcja przyjmuje więcej argumentów - oczekiwana jest tupla odpowiedniej
# długości, np. two_args_function_name=(1, 2)

# przykład 1:
# sygnatury funkcji:
# def no_arg()
# def one_arg(a)
# def multiple_args(a, b, c, e, f)
#
# wywołanie function_results_sum:
# function_results_sum(
#     no_arg, one_arg, multiple_args,
#     one_arg=23,
#     multiple_args=(1, 2, 3, 4, 5)
# )

# inne wywołanie function_results_sum:
# function_results_sum(
#     no_arg, one_arg, multiple_args,
#     one_arg=-1245
#     multiple_args=(45, 65, 76, 123456, 111.222)
# )
#
# W zadaniu skorzystaj z atrybutu __name__ dostępnego na obiekcie funkcji
#
# Zadanie nie wymaga sprawdzania poprawności przekazywanych argumentów,
# obowiązek przekazania odpowiedniej liczby argumentów do wszystkich funkcji spoczywa na tym, kto wywołuje function_results_sum
#
# Do odpowiedniego uruchomienia funkcji przyda się operator * przy wywołaniu funkcji. Poniżej przydatne linki:
# https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists
# https://stackoverflow.com/questions/2921847/what-does-the-star-operator-mean

def function_results_sum(*functions, **function_args):
    result = 0
    for function in functions:
        arguments = function_args.get(function.__name__, ())
        if isinstance(arguments, int):
            result += function(arguments)
        else:
            result += function(*arguments)
    return result


# dane do testow

def no_arg():
    return 10


def get_double_n(n):
    return 2 * n


def get_product_of_three_values(a, b, c):
    return a * b * c


# testy poprawnosci


def test_no_arg(func):
    """Czy brak argumentów działa? (brak funkcji w kwargsach)"""
    assert func(no_arg) == 10


def test_one_arg(func):
    """Czy pojedynczy argument działa? (fname=1)"""
    assert func(get_double_n, get_double_n=20) == 40


def test_multiple_args(func):
    """Czy lista argumentów działa? (fname=(1,2,3))"""
    assert func(get_product_of_three_values, get_product_of_three_values=(3, 4, 5)) == 60


def test_all_types_of_args(func):
    """Czy wszystkie typy argumentów przeszły (całkowity brak, pojedyncza wartość I lista wartości)?"""
    result = func(
        get_product_of_three_values,
        no_arg,
        get_double_n,
        get_double_n=3,
        get_product_of_three_values=(1, 2, 6)
    )
    assert result == 28


assignment = Assignment(
    'zadanie5',
    'zadanie5.py',
    'function_results_sum',
    (
        test_no_arg,
        test_one_arg,
        test_multiple_args,
        test_all_types_of_args,
    )
)
