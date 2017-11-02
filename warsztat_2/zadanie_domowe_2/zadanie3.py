# Zadanie 3
# Napisz funkcję, add_one, która przyjmuje jako argument listę.
# Do podanej listy powinien zostać dodany nowy element: 1, a następnie lista powinna zostać zwrócona z funkcji.
# Argument w funkcji niech będzie opcjonalny - w przypadku, gdy funkcja nie otrzyma żadnego argumentu, niech zachowuje się tak, jakby otrzymała pustą listę.

test_list = [5, 6, 7]
result1 = add_one(test_list)
assert result1 == [5, 6, 7, 1]

result2 = add_one()
assert result2 == [1]

result3 = add_one()
assert result3 == [1]
