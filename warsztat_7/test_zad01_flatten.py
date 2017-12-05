from zad01_flatten import flatten


def test_flatten_not_nested_list():
    test_list = [1, 2, 3]

    result = flatten(test_list)

    assert result == [1, 2, 3]


def test_flatten_nested_list():
    test_list = [1, [2, 3], 4]

    result = flatten(test_list)

    assert result == [1, 2, 3, 4]


def test_flatten_empty_list():
    test_list = []

    result = flatten(test_list)

    assert result == []


def test_flatten_different_nestings():
    test_list = [[1, 2, [3, 4, 5], [6], 7, 8], 9]

    result = flatten(test_list)

    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9]
