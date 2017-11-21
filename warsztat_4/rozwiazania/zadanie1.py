from homework_checker.base import Assignment


# Zaimplementuj klasę Date, która tworzona jest na podstawie trzech wartości - day, month i year.
# Obiekt klasy powinien zawierać atrybuty day, month i year

# Twoim zadaniem jest sprawdzenie w trakcie tworzenia obiektu, czy podane wartości są poprawne:
# jeśli year nie jest intem - rzucić InvalidYearError
# jeśli month nie jest intem lub nie zawiera się w przedziale od 1 do 12 - rzucić InvalidMonthError
# jeśli day nie jest intem lub nie zawiera się w przedziale o 1 do 28/30/31 (odpowiednio w zależności od miesiąca) - rzucić InvalidDayError

# Wszystkie opisane powyżej błędy powinny dziedziczyć z bazowego błędu - DateError

# W zadaniu dla uproszczenia zakładamy, że każdy luty ma 28 dni ;)

class DateError:
    pass


class InvalidYearError(DateError):
    pass


class InvalidMonthError(DateError):
    pass


class InvalidDayError(DateError):
    pass


class Date:
    MONTH_DAYS = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                  7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    def __init__(self, day, month, year):
        if type(year) is not int:
            raise InvalidYearError
        if type(month) is not int or not 1 <= month <= 12:
            raise InvalidMonthError
        if type(day) is not int or not 1 <= day <= self.MONTH_DAYS[month]:
            raise InvalidDayError

        self.year = year
        self.month = month
        self.day = day



def has_date_error(attribute, module, attr_name):
    assert 'DateError' in dir(module)


def has_invalid_day_error(attribute, module, attr_name):
    assert 'InvalidDayError' in dir(module)


def invalid_day_error_bases_on_date_error(attribute, module, attr_name):
    assert issubclass(module.InvalidDayError, module.DateError)


def has_invalid_month_error(attribute, module, attr_name):
    assert 'InvalidMonthError' in dir(module)


def invalid_month_bases_on_date_error(attribute, module, attr_name):
    assert issubclass(module.InvalidMonthError, module.DateError)


def has_invalid_year_error(attribute, module, attr_name):
    assert 'InvalidYearError' in dir(module)


def invalid_year_error_bases_on_date_error(attribute, module, attr_name):
    assert issubclass(module.InvalidYearError, module.DateError)


def test_basic_usage(attribute, module, attr_name):
    date = attribute(30, 5, 2020)
    assert date.day == 30
    assert date.month == 5
    assert date.year == 2020


def test_check_day(attribute, module, attr_name):
    try:
        attribute(40, 5, 2020)
    except module.InvalidDayError:
        pass
    else:
        assert False


def test_check_month(attribute, module, attr_name):
    try:
        attribute(21, 13, 2020)
    except module.InvalidMonthError:
        pass
    else:
        assert False


def test_check_year(attribute, module, attr_name):
    try:
        attribute(40, 5, 'hello')
    except module.InvalidYearError:
        pass
    else:
        assert False


assignment = Assignment(
    'zadanie1',
    'zadanie1.py',
    'Date',
    (has_date_error, has_invalid_year_error, has_invalid_month_error, has_invalid_day_error,
     invalid_year_error_bases_on_date_error, invalid_month_bases_on_date_error,
     invalid_day_error_bases_on_date_error, test_basic_usage, test_check_year, test_check_month,
     test_check_day)
)
