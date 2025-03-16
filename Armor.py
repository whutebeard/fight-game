


class Armor:
    def __init__(self, name: str, protection: int, cost):
        self.__name = name
        self.__protection = protection

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def protection(self) -> int:
        return self.__protection
    

class Without(Armor):
    def __init__(self, name = "безброневая", protection = 0, cost = 0):
        super().__init__(name, protection, cost)

    
    
class Leather(Armor):
    def __init__(self, name = "Кожанка", protection = 10, cost = 1000):
        super().__init__(name, protection, cost)

class Chainmail(Armor):
    def __init__(self, name = "Кольчуга", protection = 20, cost = 1500):
        super().__init__(name, protection, cost)

class Harness(Armor):
    def __init__(self, name = "Доспехи", protection = 30, cost = 2000):
        super().__init__(name, protection, cost)

class Cursed(Armor):
    def __init__(self, name = "Проклятая", protection = -5, cost = 5000):
        super().__init__(name, protection, cost)

class Diamond(Armor):
    def __init__(self, name = "Алмазная", protection = 60, cost = 4000):
        super().__init__(name, protection, cost)

class Infinity(Armor):
    def __init__(self, name = "Бесконечная", protection = 150, cost = 5000 ):
        super().__init__(name, protection, cost)

class Universe(Armor):
    def __init__(self, name = "Вселенская", protection = 250, cost = 7000):
        super().__init__(name, protection, cost)

class Multiverse(Armor):
    def __init__(self, name = 'Мультивселенская', protection = 300, cost = 10000):
        super().__init__(name, protection, cost)

    
