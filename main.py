import os
import os.path
import pathlib
from random import randint
from time import sleep
import json


from Weapon import Spear, TrueTripleKatana, DaggerWithPoison, Stick, Sword, Gun, Minigun, Braid, Hands
from Armor import Leather, Without, Diamond, Harness, Chainmail, Cursed, Universe, Infinity
from Wizard import Wizard
from Wariorr import Warrior
from change_money import n, n_1




print('------------------')
print(os.getcwd()) # Путь к месту запуска
print(pathlib.Path(__file__).parent.resolve()) # Путь к папке, где лежит этот скрипт
print('------------------')




ALL_WEAPONS_COUNT = 9
ALL_ARMORS_COUNT = 8


def provide_warrior(unit: Warrior):
    all_weapons = [Spear(), TrueTripleKatana(), DaggerWithPoison(), Stick(), Sword(), Gun(), Minigun(), Braid(), Hands()]
    a = input('Какое оружие вы хотите выбрать?\nНапишите его название тут\n')
    for i in range(len(all_weapons)):
        if a == all_weapons[i].name:
            unit.add_weapon(all_weapons[i])
        break


    all_armors = [Leather(), Without(), Diamond(), Harness(), Chainmail(), Cursed(), Universe(), Infinity()]
    b = input('Какое броню вы хотите взять?\nНапишите его название тут\n')
    for i in range(len(all_armors)):
        if b == all_armors[i].name:
            unit.add_armor(all_armors[i])
            break

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
        unit_a.__money = n.read()
        print(f'{unit_a.name} в кровавой схватке победил {unit_b.name}, у него осталось {unit_a.health} хп\n Теперь у {unit_a.name} {unit_a.__money}  денег\n У {unit_a.name}  уровень ')
    else:
        unit_b.__money = n_1.read()
        print(f'{unit_b.name} в кровавой схватке победил {unit_a.name}, у него осталось {unit_b.health} хп\n Теперь у {unit_b.name} {unit_b.__money} денег\n У {unit_b.name}  уровень')