from Armor import Without, Leather, Harness, Chainmail, Cursed, Diamond, Infinity, Universe, Multiverse
from random import randint

class Weapon:
    def __init__(self, name: str, damage: int):
        self.__name = name
        self.__damage = damage

    def _get_damage(self, armor, l, w, ch, h, d, i, u, mv):
        if armor is Leather:
            return self.damage - l
        elif armor is Without:
            return self.damage - w
        elif armor is Chainmail:
            return self.damage - ch
        elif armor is Harness:
            return self.damage - h
        elif armor is Diamond:
            return self.damage - d
        elif armor is Infinity:
            return self.damage - i
        elif armor is Universe:
            return self.damage * u
        elif armor is Multiverse:
            return self.damage * mv
        else:
            m = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3]
            return self.damage + m[randint(0, 9)]

    
    def get_armor(self, armor):
        return 0

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def damage(self) -> int:
        return self.__damage
    
class Spear(Weapon):
    def __init__(self, name = "Копье", damage = 40):
        super().__init__(name, damage)

    def get_damage(self, armor):
        self._get_damage(armor, 1, 0, 3, 5, 7, 9, 0.25, 0.1)
        
class Sword(Weapon):
    def __init__(self, name = "Меч", damage =  30):
        super().__init__(name, damage)

    def get_damage(self, armor):
        self._get_damage(armor, 1, 0, 3, 5, 7, 9, 0.25, 0.1)
        

class Braid(Weapon):
    def __init__(self, name = "Коса", damage = 50):
        super().__init__(name, damage)
    def get_damage(self, armor):
        self._get_damage(armor, 0, 0, 2, 6, 8, 0.25, 0.1)

class Stick(Weapon):
    def __init__(self, name = "Палка", damage = 24):
        super().__init__(name, damage)
    def get_damage(self, armor):
        self._get_damage(armor, 1, 0 , 4, 7, 7, 9, 0.25, 0.1)

class Hands(Weapon):
    def __init__(self, name = "Руки", damage = 14):
        super().__init__(name, damage)
    def get_damage(self, armor):
        self._get_damage(armor, 1, 0, 4, 5, 7, 8, 0.25, 0.1)

class DaggerWithPoison(Weapon):
    def __init__(self, name = "Кинжал с ядом", damage = 12):
        super().__init__(name, damage)
    def get_damage(self, armor):
        self._get_damage(armor, 1, 0, 3, 5, 7, 9, 0.25, 0.1)
        
class TrueTripleKatana(Weapon):
    def __init__(self, name = "Истинная тройная катана", damage = 100):
        super().__init__(name, damage)

    def get_damage(self, armor):
        self._get_damage(armor, 1, 0, 5, 3, 6, 7, 0.25, 0.1)

class Gun(Weapon):
    def __init__(self, name = "Пистолет правды", damage = 140):
        super().__init__(name, damage)
    
    def get_damage(self, armor):
        self._get_damage(armor, 1, 0, 3, 5, 7, 9, 0.25, 0.1)


class Minigun(Weapon):
    def __init__(self, name = "Пулемет ненависти", damage = 170):
        super().__init__(name, damage)
    
    def get_damage(self, armor):
        self._get_damage(armor, 1, 0, 3, 5, 7, 9, 0.25, 0.1)
        


    