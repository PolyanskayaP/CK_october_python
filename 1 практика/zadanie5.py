import random
from random import randint
import string

length = 9
letters = string.ascii_lowercase
name = ''.join(random.choice(letters) for i in range(length))

age = randint(1, 121)

ka_list = ['ЕЕ', 'ШЕ', 'ПП', 'ШК']   #да что такое этот ваш класс апа.....
ka = random.choice(ka_list)

har_udacha = randint(0, 101)
har_trud = randint(0, 101)
har_nastroenie = randint(0, 101)

par_skorost = randint(1, 15)
par_zdor = randint(0,101)
par_soprotivl = randint(0, 101)

navik_list = ['прыгает четверной', 'умеет летать', 'не стареет', 'умеет телепортироваться', 'хакер', 'ест ёжиков', 'открывает любую дверь', \
    'стирает память врагам', 'стреляет огнём', 'виртуозно кидается тетрадями', 'замораживает предметы', 'читает мысли других']
naviki = random.sample(navik_list, k=randint(1, len(navik_list)))

print("имя:", name)
print("возраст:", age)
print("класс апа:", ka)
print("скорость:", par_skorost, "км/ч пешком")
print("здоровье:", par_zdor)
print("сопротивляемость ударам:", par_soprotivl)
print("удача:", har_udacha)
print("трудолюбие:", har_trud)
print("настроение:", har_nastroenie)
print("навыки:", naviki)