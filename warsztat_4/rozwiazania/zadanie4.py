from homework_checker.base import Assignment

class Picture():
    def __init__(self, red, green, blue, width, height):
        self.r = list(red)  # tworzymy nową listę, żeby się uniezależnić od przyszłych zmian w rgb poza naszą klasą
        self.g = list(green)
        self.b = list(blue)
        self.w = width
        self.h = height

    def red(self):
        return tuple(self.r)

    def green(self):
        return tuple(self.g)

    def blue(self):
        return tuple(self.b)

    def size(self):
        return self.w, self.h

    def pixel(self, x, y):
        pixel_index = self._get_pixel_index(x, y)
        r = self.r[pixel_index]
        g = self.g[pixel_index]
        b = self.b[pixel_index]
        return r, g, b

    def _get_pixel_index(self, x, y):
        return x + y * self.w

    def crop(self, x, y, width, height):
        new_r = []
        new_b = []
        new_g = []
        width = min(width, self.w - x)
        height = min(height, self.h - y)
        for i in range(height):
            start_idx = self._get_pixel_index(x, y + i)
            end_idx = self._get_pixel_index(x + width, y + i)
            new_r.extend(self.r[start_idx:end_idx])
            new_g.extend(self.g[start_idx:end_idx])
            new_b.extend(self.b[start_idx:end_idx])
        self.r = new_r
        self.g = new_g
        self.b = new_b
        self.w = width
        self.h = height


def test_one_red_pixel():
    red = [255]
    green = [0]
    blue = [0]
    width = 1
    height = 1
    obrazek = Picture(red=red, green=green, blue=blue, width=width, height=height)
    assert (1, 1) == obrazek.size()
    assert (255,) == obrazek.red()
    assert (0,) == obrazek.green()
    assert (0,) == obrazek.blue()
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
    obrazek_2.crop(0, 0, 16, 16)  # powinniśmy dostac ten sam obrazek
    assert obrazek.red() == obrazek_2.red()
    assert obrazek.green() == obrazek_2.green()
    assert obrazek.blue() == obrazek_2.blue()

    # Left upper corner
    obrazek_2 = Picture(red=range(256), green=range(256), blue=range(256), width=16, height=16)
    obrazek_2.crop(0, 0, 1, 1)
    assert (0,) == obrazek_2.red()
    assert (0,) == obrazek_2.green()
    assert (0,) == obrazek_2.blue()

    # right upper corner
    obrazek_2 = Picture(red=range(256), green=range(256), blue=range(256), width=16, height=16)
    obrazek_2.crop(15, 0, 1, 1)
    assert (15,) == obrazek_2.red()
    assert (15,) == obrazek_2.green()
    assert (15,) == obrazek_2.blue()

    # right lower corner
    obrazek_2 = Picture(red=range(256), green=range(256), blue=range(256), width=16, height=16)
    obrazek_2.crop(15, 15, 1, 1)
    assert (255,) == obrazek_2.red()
    assert (255,) == obrazek_2.green()
    assert (255,) == obrazek_2.blue()

    # left lower corner
    obrazek_2 = Picture(red=range(256), green=range(256), blue=range(256), width=16, height=16)
    obrazek_2.crop(0, 15, 1, 1)
    assert (240,) == obrazek_2.red()
    assert (240,) == obrazek_2.green()
    assert (240,) == obrazek_2.blue()

    # 2x3 near lower corner
    obrazek_2 = Picture(red=range(256), green=range(256), blue=range(256), width=16, height=16)
    obrazek_2.crop(1, 12, 2, 3)
    assert (193, 194, 209, 210, 225, 226) == obrazek_2.red()
    assert (193, 194, 209, 210, 225, 226) == obrazek_2.green()
    assert (193, 194, 209, 210, 225, 226) == obrazek_2.blue()

    # 10x15 wystający → 3x5 lower right corner
    obrazek_2 = Picture(red=range(256), green=range(256), blue=range(256), width=16, height=16)
    obrazek_2.crop(13, 11, 10, 15)
    assert (189, 190, 191, 205, 206, 207, 221, 222, 223, 237, 238, 239, 253, 254,
            255) == obrazek_2.red()
    assert (189, 190, 191, 205, 206, 207, 221, 222, 223, 237, 238, 239, 253, 254,
            255) == obrazek_2.green()
    assert (189, 190, 191, 205, 206, 207, 221, 222, 223, 237, 238, 239, 253, 254,
            255) == obrazek_2.blue()


def test_prostokat_gradient():
    obrazek = Picture(red=range(256), green=range(256), blue=range(256), width=64, height=4)
    assert (64, 4) == obrazek.size()
    val = 0
    for y in range(4):
        for x in range(64):
            assert (val, val, val) == obrazek.pixel(x, y)
            val += 1

    # Same picture
    obrazek_2 = Picture(red=range(256), green=range(256), blue=range(256), width=64, height=4)
    obrazek_2.crop(0, 0, 64, 4)  # powinniśmy dostac ten sam obrazek
    assert obrazek.red() == obrazek_2.red()
    assert obrazek.green() == obrazek_2.green()
    assert obrazek.blue() == obrazek_2.blue()

    # Left upper corner
    obrazek_2 = Picture(red=range(256), green=range(256), blue=range(256), width=64, height=4)
    obrazek_2.crop(0, 0, 1, 1)
    assert (0,) == obrazek_2.red()
    assert (0,) == obrazek_2.green()
    assert (0,) == obrazek_2.blue()

    # right upper corner
    obrazek_2 = Picture(red=range(256), green=range(256), blue=range(256), width=64, height=4)
    obrazek_2.crop(63, 0, 1, 1)
    assert (63,) == obrazek_2.red()
    assert (63,) == obrazek_2.green()
    assert (63,) == obrazek_2.blue()

    # right lower corner
    obrazek_2 = Picture(red=range(256), green=range(256), blue=range(256), width=64, height=4)
    obrazek_2.crop(63, 3, 1, 1)
    assert (255,) == obrazek_2.red()
    assert (255,) == obrazek_2.green()
    assert (255,) == obrazek_2.blue()

    # left lower corner
    obrazek_2 = Picture(red=range(256), green=range(256), blue=range(256), width=64, height=4)
    obrazek_2.crop(0, 3, 1, 1)
    assert (192,) == obrazek_2.red()
    assert (192,) == obrazek_2.green()
    assert (192,) == obrazek_2.blue()

    # 2x3 near lower corner
    obrazek_2 = Picture(red=range(256), green=range(256), blue=range(256), width=64, height=4)
    obrazek_2.crop(1, 1, 2, 3)
    assert (65, 66, 129, 130, 193, 194) == obrazek_2.red()
    assert (65, 66, 129, 130, 193, 194) == obrazek_2.green()
    assert (65, 66, 129, 130, 193, 194) == obrazek_2.blue()

    # 15x15 wystający → 5x3 lower right corner
    obrazek_2 = Picture(red=range(256), green=range(256), blue=range(256), width=64, height=4)
    obrazek_2.crop(59, 1, 15, 15)
    assert (123, 124, 125, 126, 127, 187, 188, 189, 190, 191, 251, 252, 253, 254,
            255) == obrazek_2.red()
    assert (123, 124, 125, 126, 127, 187, 188, 189, 190, 191, 251, 252, 253, 254,
            255) == obrazek_2.green()
    assert (123, 124, 125, 126, 127, 187, 188, 189, 190, 191, 251, 252, 253, 254,
            255) == obrazek_2.blue()


assignment = Assignment(
    'zadanie4',
    'zadanie4.py',
    'Vector',
    (test_one_red_pixel, test_kwadrat_gradient, test_prostokat_gradient)
)
