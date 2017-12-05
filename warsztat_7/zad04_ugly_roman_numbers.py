import pytest

# UWAGA! Ten kod jest specjalnie napisany brzydko :)


def get_roman_number(arabic):
    number_m = get_m(arabic)
    arabic -= 1000 * len(number_m)
    number_d = get_d(arabic)
    arabic -= 500 * len(number_d)
    number_c = get_c(arabic)
    arabic -= 100 * len(number_c)
    number_l = get_l(arabic)
    arabic -= 50 * len(number_l)
    number_x = get_x(arabic)
    arabic -= 10 * len(number_x)
    number_v = get_v(arabic)
    arabic -= 5 * len(number_v)
    number_i = get_i(arabic)
    number_m, number_d, number_c, number_l, number_x, number_v, number_i = (
      do_magic(number_m, number_d, number_c, number_l, number_x, number_v, number_i))
    return number_m + number_d + number_c + number_l + number_x + number_v + number_i


def get_m(arabic):
    number_m = arabic // 1000
    return 'M' * number_m


def get_d(arabic):
    number_d = arabic // 500
    return 'D' * number_d

    
def get_c(arabic):
    number_c = arabic // 100
    return 'C' * number_c


def get_l(arabic):
    number_l = arabic // 50
    return 'L' * number_l


def get_x(arabic):
    number_x = arabic // 10
    return 'X' * number_x


def get_v(arabic):
    number_v = arabic // 5
    return 'V' * number_v


def get_i(arabic):
    number_i = arabic
    return 'I' * number_i
            
def do_magic(number_m, number_d, number_c, number_l,
             number_x, number_v, number_i):
  if len(number_c) == 4 and len(number_d) == 1:
      number_d = ''
      number_c = 'CM'
  elif len(number_c) == 4 and len(number_d) == 0:
      number_d = ''
      number_c = 'CD'        
  if len(number_x) == 4 and len(number_l) == 1:
      number_l = ''
      number_x = 'XC'
  elif len(number_x) == 4 and len(number_l) == 0:
      number_l = ''
      number_x = 'XL'
  if len(number_i) == 4 and len(number_v) == 1:
      number_i = ''
      number_v = 'IX',
  elif len(number_i) == 4 and len(number_v) == 0:
      number_ii = 'IV'
  return (number_m, number_d, number_c, number_l,
    number_x, number_v, number_i)


num = input()
roman = get_roman_number(int(num))
print(roman)
