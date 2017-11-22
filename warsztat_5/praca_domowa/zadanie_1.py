# Iterator Collatza
#
# Zadanie rozwiąż BEZ UŻYCIA GENERATORÓW.
# Napisz klasę CollatzSeq(start_value) wyliczającą kolejne liczby według wzoru:
#    https://pl.wikipedia.org/wiki/Problem_Collatza#Sformu.C5.82owanie_problemu_Collatza
# Powinno być możliwe iterowanie po CollatzSeq (po kolejnych liczbach z sekwencji).
# Wartość 1 powinna być zwrócona tylko raz, potem iteracja powinna zostać przerwana
# 
# Argumenty:
#     `start_value` - liczba od której zaczniemy wyliczać sekwencję. Podanie liczby innej niż 
#                            liczba naturalna powinno skutkować rzuceniem wyjątku ValueError


def test_invalid_start(start):
    raised = False
    try:
        a = CollatzSeq(start)
    except ValueError as e:
        raised = True
    assert raised


if __name__ == '__main__':
    assert list(CollatzSeq(1)) == [1]
    assert list(CollatzSeq(2)) == [2, 1]
    assert list(CollatzSeq(3)) == [3, 10, 5, 16, 8, 4, 2, 1]
    assert list(CollatzSeq(12)) == [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
    assert list(CollatzSeq(19)) == [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    assert list(CollatzSeq(27)) == [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    assert list(CollatzSeq(12346789)) == [12346789, 37040368, 18520184, 9260092, 4630046, 2315023, 6945070, 3472535, 10417606, 5208803, 15626410, 7813205, 23439616, 11719808, 5859904, 2929952, 1464976, 732488, 366244, 183122, 91561, 274684, 137342, 68671, 206014, 103007, 309022, 154511, 463534, 231767, 695302, 347651, 1042954, 521477, 1564432, 782216, 391108, 195554, 97777, 293332, 146666, 73333, 220000, 110000, 55000, 27500, 13750, 6875, 20626, 10313, 30940, 15470, 7735, 23206, 11603, 34810, 17405, 52216, 26108, 13054, 6527, 19582, 9791, 29374, 14687, 44062, 22031, 66094, 33047, 99142, 49571, 148714, 74357, 223072, 111536, 55768, 27884, 13942, 6971, 20914, 10457, 31372, 15686, 7843, 23530, 11765, 35296, 17648, 8824, 4412, 2206, 1103, 3310, 1655, 4966, 2483, 7450, 3725, 11176, 5588, 2794, 1397, 4192, 2096, 1048, 524, 262, 131, 394, 197, 592, 296, 148, 74, 37, 112, 56, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    test_invalid_start(0)
    test_invalid_start(-12)
    test_invalid_start(2.0)
    test_invalid_start("111")
