# task_1_1.pу - знакомство с модулями
import sys

print("Версия Python:", sys.version.split()[0])
print ("Интерпретатор:", sys. executable)

print ("Количество путей поиска:", len(sys.path))
for p in sys.path[:4]:
    print("  ", p)

import math, random

print("math.pi =", math.pi)
print("random.random() =", random.random())

mods = sorted(sys.modules)
print("Всего загружено модулей:", len (mods))
print ("Пример: ", mods[:5])

# TODO 1: выведите количество публичных имён в модуле math
public = [n for n in dir(math) if not n.startswith('.')]
print ("Публичных имён в math:", len(public))
print ("Первые 8:", public[:8])

# TODO 2: выведите _namе_ и _file_ этого скрипта
print ("Мой _name_ =", __name__)
#Если создать свою библиотеку с таким же названием как у random, то она будет с ней конфлитовать
#из-за того, что модуль random импортируется в модуль __main__ и в вашу библиотеку тоже импортируется.
#Ваша библиотека будет использовать функцию random из модуля random, а не вашу.
