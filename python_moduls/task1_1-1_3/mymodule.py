"""Небольшой модуль с геометрическими функциями.
Содержит константу PI, версию модуля и функции для вычисления
площади круга, длины окружности и объёма шара.
"""

PI = 3.141592653589793
VERSION = '1.0.0'
_secret = 'This is secret'

def circle_area(r):
    """Вернуть площадь круга радиусом r (S = pi * r^2)."""
    return PI * r ** 2

def circle_len(r):
    """Вернуть длину окружности радиусом r (L = 2 * pi * r)."""
    return 2* PI * r

def sphere_volume(r):
        """Вернуть объём шара радиусом r.

    Формула: V = 4/3 * pi * r^3.

    Пример:
        >>> round(sphere_volume(1), 4)
        4.1888
    """
        return 4/3 * PI * r ** 3

def _helper(): return PI/2

if __name__ == '__main__':
    print(f'[{VERSION}] Самопроверка mymodule:')
    print(' S(r=2) = ', circle_area(2))
    print(' L(r=2) = ', circle_len(2))