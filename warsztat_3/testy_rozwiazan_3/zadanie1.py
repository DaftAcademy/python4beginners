from homework_checker.base import Assignment


#
# Treść zadania
#

# # Rozwinięcie przykładu z zajęć
# # Na zajęciach pisaliśmy klasę Vector.
#
# class Vector():
# 	def __init__(self, *args):
# 		# print(args)
# 		self.coords = list(args)
#
# 	def __repr__(self):
# 		template = '{}({})'
# 		name = self.__class__.__name__
# 		args = ', '.join(repr(x) for x in self.coords)
# 		# print(name, args)
# 		return template.format(name, args)
#
# 	def __add__(self, other):
# 		tmp = []
# 		for i in range(len(self)):
# 			tmp.append(self.coords[i] + other.coords[i])
# 		return Vector(*tmp)
#
# 	def __iadd__(self, other):
# 		for i in range(len(self)):
# 			self.coords[i] += other.coords[i]
# 		return self
#
# 	def __len__(self):
# 		return len(self.coords)
#
# 	def __eq__(self, other):
# 		for i in range(len(self)):
# 			if not self.coords[i] == other.coords[i]:
# 				return False
# 		return True
#
# # Zadaniem domowym jest rozszerzenie funkcjonalności i refactor już istniejących.
# # Trzeba zmodyfikować kod klasy Vector nie psując obecnych funkcjonalności.
# # W pracy domowej proszę zamieścić tylko kod klasy Vector, żadnych assertów/printów .
#
# # Chcemy mieć możliwość uzyskania wartości konkretnej współrzędnej po indeksie
#
# v = Vector(1, 2, 3, 4)
# assert 1 == v[0]
# assert 2 == v[1]
# assert 3 == v[2]
# assert 4 == v[3]
#
# assert 4 == v[-1]
#
# # Chcemy mieć możliwość ustawienia wartości konkretnej współrzędnej
#
# v1 = Vector(3, 4, 8)
# v1[2] = 5
# assert 'Vector(3, 4, 5)' == str(v1)
#
# # Jeżeli powyższe dwa polecenia zostały wykonane "sprytnie" to powinniśmy
# # mieć teraz możliwość iterowania po współrzędnych wektora
#
# v2 = Vector(4, 6, 8, 10, 12)
# dumped = [x for x in v2]
# assert [4, 6, 8, 10, 12] == dumped
#
# # Dzięki temu możemy w funkcjach "magicznych" pozbyć się odwołań do implementacji vectora.
# # Odwołania do other.coords są już niepotrzebne i większość self.coords też.
# # Należy je zastąpić czymś innym - to już wasze zadanie wymyślić i zaprogramować.
# # Chcemy zapewnić sobie możliwość "duck typing".
#
# looks_like_vector = [0, 1, 2, 3]
# v3 = Vector(3, 2, 1, 0)
# v4 = v3 + looks_like_vector
# v5 = looks_like_vector + v3
# assert v4 == v5
# assert isinstance(v4, Vector)
# assert isinstance(v5, Vector)
# assert 'Vector(3, 3, 3, 3)' == str(v4)
#
# v6 = Vector(0, 1, 2, 3)
# assert v6 == looks_like_vector
# assert looks_like_vector == v6

#
# Przykładowe rozwiązanie:
#

class Vector():
    def __init__(self, *args):
        # print(args)
        self.coords = list(args)

    def __repr__(self):
        template = '{}({})'  # chcemy osiągnąć NazwaKlasy(argumenty, oddzielone, przecinkami)
        name = self.__class__.__name__
        args = ', '.join(repr(x) for x in self)
        return template.format(name, args)

    def __add__(self, other):
        tmp = [x + y for x, y in zip(self, other)]
        # for i in range(len(self)):
        # 	tmp.append(self.coords[i] + other.coords[i])=
        return Vector(*tmp)

    def __iadd__(self, other):
        for i, v in enumerate(other):
            self[i] += v
        return self

    def __radd__(self, other):
        return self + other

    def __len__(self):
        return len(self.coords)

    def __eq__(self, other):
        for x, y in zip(self, other):
            if not x == y:
                return False
        return True

    def __getitem__(self, idx):
        return self.coords[idx]

    def __setitem__(self, idx, value):
        self.coords[idx] = value


#
# testy poprawności
#

def has_getitem(cls):
    """Czy zdefiniowano metodę '__getitem__'?"""
    assert hasattr(cls, '__getitem__')


def getitem_works_properly(cls):
    """Czy używając dostępu przez indeks otrzymujemy odpowiednie wartości?"""
    v = cls(1, 2, 3, 4)
    assert 1 == v[0]
    assert 2 == v[1]
    assert 3 == v[2]
    assert 4 == v[3]
    assert 4 == v[-1]


def has_setitem(cls):
    """Czy zdefiniowano metodę '__set_item__'?"""
    assert hasattr(cls, '__setitem__')


def setitem_works_properly(cls):
    """Czy używając przypisania przez indeks ustawiamy odpowiednie wartości?"""
    v1 = cls(3, 4, 8)
    v1[2] = 5
    assert v1[2] == 5


def iterate_over_elements(cls):
    """Czy iterowanie po elementach wektora działa poprawnie?"""
    v2 = cls(4, 6, 8, 10, 12)
    dumped = [x for x in v2]
    assert [4, 6, 8, 10, 12] == dumped


def check_eq(cls):
    """Czy operator __eq__ działa poprawnie?"""
    v1, v2 = cls(0, 1, 2, 3), cls(0, 1, 2, 3)
    v3, v4 = cls(0, 1, 2, 3), cls(0, 2, 2, 3)
    assert v1 == v2
    assert not v1 == v2


def add_vectors(cls):
    """Czy można dodawać do siebie obiekty tej samej klasy?"""
    v1, v2 = Vector(0, 1, 2, 3), Vector(4, 5, 6, 7)
    ex = Vector(4, 6, 8, 10)
    assert ex == v1 + v2


def add_like_vectors(cls):
    """Czy można dodawać obiekty "podobne" do naszej klasy?"""
    looks_like_vector = [0, 1, 2, 3]
    v3 = Vector(3, 2, 1, 0)
    v4 = v3 + looks_like_vector
    v5 = looks_like_vector + v3
    assert v4 == v5
    assert isinstance(v4, Vector)
    assert isinstance(v5, Vector)
    assert 'Vector(3, 3, 3, 3)' == str(v4)


def comparison_with_list(cls):
    """Czy można porównywać z listą?"""
    looks_like_vector = [0, 1, 2, 3]
    v6 = Vector(0, 1, 2, 3)
    assert v6 == looks_like_vector
    assert looks_like_vector == v6


def check_inheritance_hierarchy(cls):
    """Czy klasa dziedziczy tylko i wyłącznie po typie 'object'?"""
    assert cls.mro() == [cls, object]


def check_len(cls):
    """Czy działa obliczanie długości wektora?"""
    v = cls(1, 2)
    assert 2 == len(v)
    v1 = cls(2, 4, 5.6, 7, 8)
    assert 5 == len(v1)


assignment = Assignment(
    'zadanie1',
    'zadanie1.py',
    'Vector',
    (has_getitem, getitem_works_properly, has_setitem, setitem_works_properly,
     iterate_over_elements, add_vectors, add_like_vectors, comparison_with_list,
     check_inheritance_hierarchy, check_len)
)
