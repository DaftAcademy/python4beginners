from homework_checker.base import Assignment


# Zadanie 3
# Napisz funkcję, add_one, która przyjmuje jako argument listę.
# Do podanej listy powinien zostać dodany nowy element: 1, a następnie lista powinna zostać zwrócona z funkcji.
# Argument w funkcji niech będzie opcjonalny - w przypadku, gdy funkcja nie otrzyma żadnego argumentu, niech zachowuje się tak, jakby otrzymała pustą listę.


def add_one(given_list=None):
    if given_list is None:
        given_list = []
    given_list.append(1)
    return given_list


# test poprawnosci


def basic_test(func):
    """Czy działa podstawowa funkcjonalność?"""
    test_list = [5, 6, 7]
    assert func(test_list) == [5, 6, 7, 1]


def default_arg(func):
    """Czy domyślny argument został poprawnie obsłużony? (każdorazowo powinna być tworzona nowa lista)"""
    assert func() == [1]
    assert func() == [1]


def is_none_used(func, module):
    """Czy został wykorzystany `is None`?"""
    class stupid_list(list):
        def __eq__(self, other):
            # self == None returns True, but self is None doesn't
            return True
    module.list = stupid_list
    test_list = stupid_list([5, 6, 7])
    result = func(test_list)
    module.list = list
    assert [5, 6, 7, 1] == result


def empty_list_as_arg(func):
    """Czy podanie pustej listy działa poprawnie (wynik == [1])?"""
    test_list = []
    assert func(test_list) == [1]


assignment = Assignment(
    'zadanie3',
    'zadanie3.py',
    'add_one',
    (
        basic_test,
        default_arg,
        is_none_used,
        empty_list_as_arg,
    )
)
