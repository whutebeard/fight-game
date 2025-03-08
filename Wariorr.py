


class Warrior:
    def __init__(self, name: str, level: int, need_xp: int, give_xp: int, hp = 200 ):
        self.__name = name
        self.__hp = hp
        self.__armor = None
        self.__weapon = None
        self.__level = level
        self.__need_xp = need_xp
        self.__give_xp = give_xp

    @property
    def health(self) -> int:
        return self.__hp
    
    @health.setter
    def health(self, value):
        if self.health + value < 0:
            self.__hp = 0
        else:
            self.__hp = value

    

    @property
    def name(self):
        return self.__name
    
    @property
    def is_alive(self):
        return self.health > 0
    
    @property
    def armor(self):
        return self.__armor
    
    @property
    def weapon(self):
        return self.__weapon
    


    @property
    def need_xp(self):
        return self.__need_xp
    
    @property
    def level(self):
        return self.__level
    
    @property
    def give_xp(self):
        return self.__give_xp
    

    
    
    def add_weapon(self, weapon):
        self.__weapon = weapon

    def add_armor(self, armor):
        self.__armor = armor

    def add_money(self, money):
        self.__money = money
        

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
