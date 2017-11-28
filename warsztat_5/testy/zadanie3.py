from homework_checker.base import Assignment


# Fibonacci generator
#
# Napis generator ciągu Fibonacciego: fibonnacci(elements_limit).
# Generator ma zwracać kolejne wyrazy ciągu Fibonacciego: https://pl.wikipedia.org/wiki/Ci%C4%85g_Fibonacciego
#
# Args:
#    `elements_limit` - określa ilość zwróconych liczb. Jeśli `elements_limit` nie zostanie podane to generator ma być nieograniczony. Załóż, że jeżeli `elements_limit` będzie podane to zawsze będzie to int >= 0.


def test_10(func):
    assert list(func(10)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_1(func):
    assert list(func(1)) == [0]


def test_0(func):
    assert list(func(0)) == []


def test_2(func):
    assert list(func(2)) == [0, 1]


def test_infitnite(func):
    ten = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    no_limits = func()
    for x, y in zip(no_limits, ten):
        assert x == y


assignment = Assignment('zadanie3', 'zadanie3.py', 'fibonnacci',
                        (test_0, test_1, test_2, test_10, test_infitnite))
