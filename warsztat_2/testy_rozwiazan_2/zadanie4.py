from homework_checker.base import Assignment


# Zadanie 4
# Napisz funkcję factorial, która dla danego n obliczy rekurencyjnie silnię

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


# test poprawnosci


def basic_test(func):
    """Czy zwraca poprawny wynik dla argumentu 5?"""
    return func(5) == 120


def test_one(func):
    """Czy zwraca poprawny wynik dla argumentu 1?"""
    return func(1) == 1


def test_zero(func):
    """Czy zwraca poprawny wynik dla argumentu 0?"""
    return func(0) == 1


def counted(f):
    def wrapped(*args, **kwargs):
        wrapped.calls += 1
        return f(*args, **kwargs)

    wrapped.calls = 0
    return wrapped


def recurrency_used(func, module, attr_name):
    """Czy rozwiazanie jest rekurencyjne (wywołuje samo siebie)?"""
    wrapped = counted(func)
    setattr(module, attr_name, wrapped)
    wrapped(5)
    setattr(module, attr_name, func)
    assert wrapped.calls > 1


assignment = Assignment(
    'zadanie4',
    'zadanie4.py',
    'factorial',
    (
        basic_test,
        test_one,
        test_zero,
        recurrency_used,
    )
)
