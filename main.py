import os
import os.path
import pathlib
from random import randint
from time import sleep

from Weapon import Spear, TrueTripleKatana, DaggerWithPoison, Stick, Sword, Gun, Minigun, Braid, Hands
from Armor import Leather, Without, Diamond, Harness, Chainmail, Cursed, Universe, Infinity
from Wizard import Wizard
from Wariorr import Warrior

print('------------------')
print(os.getcwd()) # Путь к месту запуска
print(pathlib.Path(__file__).parent.resolve()) # Путь к папке, где лежит этот скрипт
print('------------------')




ALL_WEAPONS_COUNT = 9
ALL_ARMORS_COUNT = 8


def provide_warrior(unit: Warrior):
    all_weapons = [Spear(), TrueTripleKatana(), DaggerWithPoison(), Stick(), Sword(), Gun(), Minigun(), Braid(), Hands()]
    index = randint(0, ALL_WEAPONS_COUNT - 1)
    unit.add_weapon(all_weapons[index])

    all_armors = [Leather, Without(), Diamond(), Harness(), Chainmail(), Cursed(), Universe(), Infinity()]
    index = randint(0, ALL_ARMORS_COUNT - 1)
    unit.add_armor(all_armors[index])

    unit.get_total_protection()

    




if __name__ == '__main__':
    name_a = 'Ратмир'
    name_b = 'Карим'

    unit_a = Warrior(name=name_a, level=1, need_xp=200, give_xp=300)
    provide_warrior(unit_a)

    unit_b = Warrior(name=name_b, level=1, need_xp=200, give_xp=300)
    provide_warrior(unit_b)

    print(f'{unit_a.name} - {unit_a.health}\nБроня: {unit_a.armor.name}\nОружие: {unit_a.weapon.name}\n')
    print(f'{unit_b.name} - {unit_b.health}\nБроня: {unit_b.armor.name}\nОружие: {unit_b.weapon.name}\n')

    
    


    while unit_a.is_alive and unit_b.is_alive:
        number = randint(1, 10)
        sleep(1)


        if number % 2:
            unit_a.make_attack(enemy=unit_b)
        else:
            unit_b.make_attack(enemy=unit_a)

    

    if unit_a.is_alive:
        if os.path.isfile('money_1.txt') is False:
            a = open('money_1.txt', 'w+')
            a.write(str(0))
            a.close()
            b = open('money_1.txt')
            c = b.read()
            b.close()
            b = open('money_1.txt')
            v = int(c) + 500
            v = str(v)
            b.write(str(v))
            b.close()
            n = open('money_1.txt')
        elif os.path.isfile('money_1.txt') is True:
            b = open('money_1.txt')
            c = b.read()
            b.close()
            b = open('money_1.txt', 'w+')
            v = int(c) + 500
            v = str(v)
            b.write(str(v))
            b.close()
            n = open('money_1.txt')
        print(f'{unit_a.name} в кровавой схватке победил {unit_b.name}, у него осталось {unit_a.health} хп\n Теперь у {unit_a.name} {n.read()}  денег\n У {unit_a.name} {unit_a.level} уровень ')
    else:
        if os.path.isfile('money_2.txt') is False:
            a = open('money_2.txt', 'w+')
            a.write(str(0))
            a.close
            b = open('money_2.txt', 'r')
            c = b.read()
            b.close()
            b = open('money_2.txt', 'w+')
            v = int(c) + 500
            v = str(v)
            b.write(v)
            b.close()
            n = open('money_2txt')
        elif os.path.isfile('money_2.txt') is True:
            b = open('money_2.txt')
            c = b.read()
            b.close()
            b = open('money_2.txt', 'w+')
            v = int(c) + 500
            v = str(v)
            b.write(v)
            b.close()
            n = open('money_2.txt')
        print(f'{unit_b.name} в кровавой схватке победил {unit_a.name}, у него осталось {unit_b.health} хп\n Теперь у {unit_b.name} {n.read()} денег\n У {unit_b.name} {unit_b.level} уровень')