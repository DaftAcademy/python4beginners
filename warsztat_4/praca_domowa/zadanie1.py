# Zaimplementuj klasę Date, która tworzona jest na podstawie trzech wartości - day, month i year.
# Obiekt klasy powinien zawierać atrybuty day, month i year

# Twoim zadaniem jest sprawdzenie w trakcie tworzenia obiektu, czy podane wartości są poprawne:
# jeśli year nie jest intem - rzucić InvalidYearError
# jeśli month nie jest intem lub nie zawiera się w przedziale od 1 do 12 - rzucić InvalidMonthError
# jeśli day nie jest intem lub nie zawiera się w przedziale o 1 do 28/30/31 (odpowiednio w zależności od miesiąca) - rzucić InvalidDayError

# Wszystkie opisane powyżej błędy powinny dziedziczyć z bazowego błędu - DateError

# W zadaniu dla uproszczenia zakładamy, że każdy luty ma 28 dni ;)

class Date:
    def __init__(self, day, month, year):
        # Tu wpisz swoje rozwiązanie (i skasuj raise NotImplementedError() :)
        raise NotImplementedError()


date = Date(30, 5, 2020)
assert date.day == 30
assert date.month == 5
assert date.year == 2020

try:
    date2 = Date(40, 5, 2020)
except InvalidDayError:
    print('Błąd wyrzucony tak jak trzeba')
else:
    print('Bez błędu, a trzeba było :(')
