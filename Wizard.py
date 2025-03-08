from time import sleep
from random import randint

class Wizard:
    def __init__(self, name: int, money, gived_money: int, need_xp: int, give_xp: int, level: int, hp = 200):
        self.__name = name
        self.__hp = hp
        self.__money = money
        self.gived_money = gived_money
        self.__armor = None
        self.__weapon = None
        self.need_xp = need_xp
        self.give_xp = give_xp
        self.level = level

    @property
    def name(self):
        return self.__name
    
    @property
    def health(self):
        return self.__hp
    
    @health.setter
    def health(self, value):
        if self.health + value < 0:
            self.__hp = 0
        else:
            self.__hp = value

    
    @property
    def mon(self):
        return self.__money
    
    @mon.setter
    def mon(self, value):
        if self.is_alive:
            self.__money += value

    @property
    def weapon(self):
        return self.__weapon
    
    @property
    def armor(self):
        return self.__armor
    

    def add_weapon(self, weapon):
        self.__weapon = weapon

    def add_armor(self, armor):
        self.__armor = armor

    def take_damage(self, weapon):
            total_damage = weapon.get_damage(self.armor)

            self.health -= total_damage



    def get_total_protection(self):
        self.health  += self.__armor.protection  


            

    def make_attack(self, enemy):
        weapon = self.weapon
        if weapon is None:
            print(f'{self.name} потерял свое оружие. Атаковать нечем')
            return
        
        enemy.take_damage(weapon)
        print(f'{self.name} атаковал {enemy.name} с помощью {weapon.name}.\n У противника осталось {enemy.health} хп')


    



    

        