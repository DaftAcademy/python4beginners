# Napisać klasę Picture(red, green, blue, width, height).
# Argumenty red, green i blue mogą być dowolnymi obiektami po których można iterować (np. listami, tuplami)
# red, green, blue będą tej samej długości.
# Każdy element red, green, blue będzie miał wartość liczby całkowitej z przedziału 0 - 255 włącznie.
# dodatkowe informacje: https://en.wikipedia.org/wiki/RGB_color_model
# Każdy element obiektów red, green, blue reprezentuje wartość konkretnego koloru dla danego piksela.
# Piksele są podane są w kolejności od lewej do prawej, od górnego do dolnego wiersza.

# Instancje klasy Picture mają mieć publicznie dostępne metody:
# red()
# green()
# blue()
# size()
# crop(x, y, width, height)
# pixel(x, y)

# red()
#     ma zwrócić tuplę, wartości kanału czerwonego w kolejności wierszami od lewego górnego do prawego dolnego

# green()
#     to samo co red ale dla kanału zielonego w kolejności wierszami od lewego górnego do prawego dolnego

# blue()
#     to samo co red i green ale dla kanału niebieskiego w kolejności wierszami od lewego górnego do prawego dolnego

# size()
#     ma zwrócić tuplę z szerokością i wysokością obrazka (ile pixeli mieści się wzdłuż i wszerz)

# crop(x, y, width, height)
#     ma obciąć obrazek ("w miejscu") do prostokąta podanego w argumentach .
#     x, y - lewy górny róg prostokąta (na pewno mieści się w obrazku)
#     width, height - szerokość i wysokość prostokąta (mogą wyjść poza obrazek)
#     jeśli prostokąt będzie wystawał poza obrazek to istotna jest tylko część wspólna obecnego obrazka i prostokąta.

# pixel(x, y)
#     ma zwrócić tuplę wartości poszczególnych kolorów w pikselu o współrzędnych x, y.
#     Kolejność kanałów w wynikowej tupli to RGB.
#     np. dla obrazka o size = (10, 21) współrzędne
#         0, 0 → lewy górny róg
#         0, 20 → prawy górny róg
#         9, 0 → lewy dolny róg
#         9, 20 → prawy dolny róg
#     na potrzeby tego zadania proszę założyć, że wszystkie współrzędne x, y będą się zawierać w obrazku

def test_one_red_pixel():
    red = [255]
    green = [0]
    blue = [0]
    width = 1
    height = 1
    obrazek = Picture(red=red, green=green, blue=blue, width=width, height=height)
    assert (1, 1) == obrazek.size()
    assert (255, ) == obrazek.red()
    assert (0, ) == obrazek.green() 
    assert (0, ) == obrazek.blue()
    assert (255, 0, 0) == obrazek.pixel(0, 0)

def test_kwadrat_gradient():
    obrazek = Picture(red=range(256), green=range(256), blue=range(256), width=16, height=16)
    assert (16, 16) == obrazek.size()
    val = 0
    for y in range(16):
        for x in range(16):
            assert (val, val, val) == obrazek.pixel(x, y)
            val += 1

    # Same picture
    obrazek_2 = Picture(red=range(256), green=range(256), blue=range(256), width=16, height=16)
    obrazek_2.crop(0, 0, 16, 16) # powinniśmy dostać ten sam obrazek
    assert obrazek.red() == obrazek_2.red()
    assert obrazek.green() == obrazek_2.green()
    assert obrazek.blue() == obrazek_2.blue()

    # Left upper corner
    obrazek_2 = Picture(red=range(256), green=range(256), blue=range(256), width=16, height=16)
    obrazek_2.crop(0, 0, 1, 1)
    assert (0, ) == obrazek_2.red()
    assert (0, ) == obrazek_2.green()
    assert (0, ) == obrazek_2.blue()

    # right upper corner
    obrazek_2 = Picture(red=range(256), green=range(256), blue=range(256), width=16, height=16)
    obrazek_2.crop(15, 0, 1, 1)
    assert (15, ) == obrazek_2.red()
    assert (15, ) == obrazek_2.green()
    assert (15, ) == obrazek_2.blue()

    # right lower corner
    obrazek_2 = Picture(red=range(256), green=range(256), blue=range(256), width=16, height=16)
    obrazek_2.crop(15, 15, 1, 1)
    assert (255, ) == obrazek_2.red()
    assert (255, ) == obrazek_2.green()
    assert (255, ) == obrazek_2.blue()

    # left lower corner
    obrazek_2 = Picture(red=range(256), green=range(256), blue=range(256), width=16, height=16)
    obrazek_2.crop(0, 15, 1, 1)
    assert (240, ) == obrazek_2.red()
    assert (240, ) == obrazek_2.green()
    assert (240, ) == obrazek_2.blue()

    # 2x3 near lower corner
    obrazek_2 = Picture(red=range(256), green=range(256), blue=range(256), width=16, height=16)
    obrazek_2.crop(1, 12, 2, 3)
    assert (193, 194, 209, 210, 225, 226) == obrazek_2.red()
    assert (193, 194, 209, 210, 225, 226) == obrazek_2.green()
    assert (193, 194, 209, 210, 225, 226) == obrazek_2.blue()

    # 10x15 wystający → 3x5 lower right corner
    obrazek_2 = Picture(red=range(256), green=range(256), blue=range(256), width=16, height=16)
    obrazek_2.crop(13, 11, 10, 15)
    assert (189, 190, 191, 205, 206, 207, 221, 222, 223, 237, 238, 239, 253, 254, 255) == obrazek_2.red()
    assert (189, 190, 191, 205, 206, 207, 221, 222, 223, 237, 238, 239, 253, 254, 255) == obrazek_2.green()
    assert (189, 190, 191, 205, 206, 207, 221, 222, 223, 237, 238, 239, 253, 254, 255) == obrazek_2.blue()

if __name__ == '__main__':
    test_one_red_pixel()
    test_kwadrat_gradient()
