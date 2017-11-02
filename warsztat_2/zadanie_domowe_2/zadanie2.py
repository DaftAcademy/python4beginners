# Zadanie 2
# Napisz funkcję copy_reversed, która przyjmuje dwie listy, list_a i list_b
# i która dodaje do listy list_b całą zawartość list_a, ale w odwróconej kolejności.
# Funkcja copy_reversed niech zwraca None.

x = [1, 2, 3]
y = [4, 5, 6]

result = copy_reversed(x, y)

assert y == [4, 5, 6, 3, 2, 1]
assert result is None
