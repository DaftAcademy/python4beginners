from homework_checker.base import Assignment


# Zadanie 6
# Jesteś administratorem Bardzo Wysokiego Budynku Biurowego BWBB.
# Masz listę ile osób znajduje się na kolejnych piętrach BWBB: `lista_osob` (czyli wartość lista_osób[5] to liczba osób na piętrze nr 5) - zawiera ona tylko liczby całkowite
# W budynku znajduje się określona liczba ewakuacyjnych klatek schodowych: `liczba_klatek_schodowych` - jest to liczba całkowita
# Każda z klatek pozwala na jednoczesne poruszanie się kilku osób obok siebie: `liczba_osob_w_rzedzie` (liczba całkowita).
# Odstęp czasowy miedzy każdym ewakuowanym rzędem osób to 1 sekunda.
# `tempo_schodzenia` to liczba sekund potrzebna na przejście jednego piętra. Uznajemy, że wszyscy schodzą w tym samym tempie
# Ewakuacja budynku zaczyna się od najwyższego piętra, piętro po piętrze w dół.
# Po jakim czasie powinna zaczynać się ewakuacja dla poszczególnych pięter żeby nie tworzyły się zatory?
# Zatory nie tworzą się wtedy, gdy osoby z wyższych minęły już piętro, które jest w danym momencie ewakuowane.
# Funkcja ewakuacja powinna zwracać listę z intami po ilu sekundach od rozpoczęcia ewakuacji budynku  na każdym piętrze zostanie włączony alarm
# czyli result[6] przechowuje po ilu sekundach został włączony alarm na szóstym piętrze

# Osoby ewakuowane same rozkładają się po równo na liczbę zejść ewakuacyjnych
# Piętro zaczyna się ewakuować od razu po uruchomieniu na nim alarmu
# Argumenty do funkcji będą przekazane po nazwie, jako keyword

def ewakuacja(lista_osob, liczba_klatek_schodowych, liczba_osob_w_rzedzie, tempo_schodzenia):
    answ = [0]  # najwyższe piętro zaczyna ewakuację natychmiast
    for liczba_osob in lista_osob[-1:0:-1]:
        max_na_zejscie = liczba_osob // liczba_klatek_schodowych
        if max_na_zejscie * liczba_klatek_schodowych < liczba_osob:
            max_na_zejscie += 1  # nie można ewakuować osoby w kawałkach

        max_rzedow = max_na_zejscie // liczba_osob_w_rzedzie
        if max_rzedow * liczba_osob_w_rzedzie < max_na_zejscie:
            max_rzedow += 1  # nie pomijamy rzędu w którym ewakuje się jedna osoba

        czas = max_rzedow + tempo_schodzenia
        answ.append(answ[-1] + czas)
    return list(reversed(answ))


# testy poprawnosci

def ground_floor_only(func):
    """Czy poprawnie działa dla samego parteru?"""
    assert [0] == func(
        lista_osob=[20],
        liczba_klatek_schodowych=2,
        liczba_osob_w_rzedzie=10,
        tempo_schodzenia=3)


def test_from_assignment_description(func):
    """Czy zadanie 6 zwraca poprawny wynik?"""
    lista_osob = [5, 10, 15]
    liczba_klatek_schodowych = 2
    liczba_osob_w_rzedzie = 1
    tempo_schodzenia = 30

    assert [73, 38, 0] == func(
        lista_osob=lista_osob,
        liczba_klatek_schodowych=liczba_klatek_schodowych,
        liczba_osob_w_rzedzie=liczba_osob_w_rzedzie,
        tempo_schodzenia=tempo_schodzenia
    )


def five_floors(func):
    """Czy dla 5 pięter dobre rozwiązanie."""
    lista_osob = [123, 456, 789, 246, 369]
    liczba_klatek_schodowych = 10
    liczba_osob_w_rzedzie = 10
    tempo_schodzenia = 3

    assert [32, 24, 13, 7, 0] == func(
        lista_osob=lista_osob,
        liczba_klatek_schodowych=liczba_klatek_schodowych,
        liczba_osob_w_rzedzie=liczba_osob_w_rzedzie,
        tempo_schodzenia=tempo_schodzenia
    )


def same_number_of_people_on_each_floor(func):
    """Czy dla jednakowej liczby osób na każdym piętrze dobre rozwiązanie."""
    lista_osob = [100] * 46
    liczba_klatek_schodowych = 2
    liczba_osob_w_rzedzie = 4
    tempo_schodzenia = 15

    assert [1260, 1232, 1204, 1176, 1148, 1120, 1092, 1064, 1036, 1008, 980, 952,
            924, 896, 868, 840, 812, 784, 756, 728, 700, 672, 644, 616, 588, 560,
            532, 504, 476, 448, 420, 392, 364, 336, 308, 280, 252, 224, 196, 168,
            140, 112, 84, 56, 28, 0] == func(
        lista_osob=lista_osob,
        liczba_klatek_schodowych=liczba_klatek_schodowych,
        liczba_osob_w_rzedzie=liczba_osob_w_rzedzie,
        tempo_schodzenia=tempo_schodzenia
    )


assignment = Assignment(
    'zadanie6',
    'zadanie6.py',
    'ewakuacja',
    (
        ground_floor_only,
        test_from_assignment_description,
        five_floors,
        same_number_of_people_on_each_floor
    )
)
