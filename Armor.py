


class Armor:
    def __init__(self, name: str, protection: int):
        self.__name = name
        self.__protection = protection

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def protection(self) -> int:
        return self.__protection
    

class Without(Armor):
    def __init__(self, name = "безброневая", protection = 0):
        super().__init__(name, protection)

    
    
class Leather(Armor):
    def __init__(self, name = "Кожанка", protection = 10):
        super().__init__(name, protection)

class Chainmail(Armor):
    def __init__(self, name = "Кольчуга", protection = 20):
        super().__init__(name, protection)

class Harness(Armor):
    def __init__(self, name = "Доспехи", protection = 30):
        super().__init__(name, protection)

class Cursed(Armor):
    def __init__(self, name = "Проклятая", protection = -5):
        super().__init__(name, protection)

class Diamond(Armor):
    def __init__(self, name = "Алмазная", protection = 60):
        super().__init__(name, protection)

class Infinity(Armor):
    def __init__(self, name = "Бесконечная", protection = 150):
        super().__init__(name, protection)

class Universe(Armor):
    def __init__(self, name = "Вселенская", protection = 250):
        super().__init__(name, protection)


    
