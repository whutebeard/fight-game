import os
import os.path
import pathlib
from random import randint
from time import sleep
import keyword


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
    a = input('Какое оружие вы хотите выбрать?\nНапишите его название тут\n')
    for i in range(len(all_weapons)):
            if a == all_weapons[i].name:
                unit.add_weapon(all_weapons[i])
                if unit.weapon.cost < unit.money:
                    unit.weapon = unit.weapon
                else:
                    unit.weapon = all_weapons[ALL_WEAPONS_COUNT-1]       
            break


    all_armors = [Leather(),  Infinity(), Diamond(), Harness(), Chainmail(), Cursed(), Universe(), Without()]
    b = input('Какое броню вы хотите взять?\nНапишите его название тут\n')
    for i in range(len(all_armors)):
        if b == all_armors[i].name:
                unit.add_armor(all_armors[i])
                if unit.armor.cost < unit.money:
                     unit.armor = unit.armor
                else:
                    unit.armor = all_armors[ALL_ARMORS_COUNT-1]
                break

    unit.get_total_protection()

    




if __name__ == '__main__':
    name_a = 'Ратмир'
    name_b = 'Карим'

    

    unit_a = Warrior(name=name_a, need_xp=200, give_xp=300)
    provide_warrior(unit_a)

    unit_b = Warrior(name=name_b, need_xp=200, give_xp=300)
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
        unit_a.set_money('money_1.txt')
        unit_a.set_level('level_1.txt', 'need_xp_1.txt', 'give_xp_1.txt')
        print(f'{unit_a.name} в кровавой схватке победил {unit_b.name}, у него осталось {unit_a.health} хп\n Теперь у {unit_a.name} {unit_a.money}  денег\n У {unit_a.name} {unit_a.level}  уровень ')
    else:
        unit_b.set_money('money_2.txt')
        unit_b.set_level('level_2.txt', 'need_xp_2.txt', 'give_xp_2.txt')
        print(f'{unit_b.name} в кровавой схватке победил {unit_a.name}, у него осталось {unit_b.health} хп\n Теперь у {unit_b.name} {unit_b.money} денег\n У {unit_b.name} {unit_b.level} уровень')