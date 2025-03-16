import os.path


class Warrior:
    def __init__(self, name: str,  need_xp: int, give_xp: int, money = 0, hp = 200, level = 1 ):
        self.__name = name
        self.__hp = hp
        self.__armor = None
        self.__weapon = None
        self.level = level
        self.need_xp = need_xp
        self.give_xp = give_xp
        self.money = money

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
    



    
    
    def add_weapon(self, weapon):
        self.__weapon = weapon

    def add_armor(self, armor):
        self.__armor = armor

    def set_money(self, file):
            if os.path.isfile(file) is False:
                a = open(file, 'w+')
                a.write(str(self.money))
                a.close()
                b = open(file)
                c = b.read()
                b.close()
                b = open(file  , 'w+')
                v = int(c) + 500
                v = str(v)
                b.write(str(v))
                b.close()
                n = open(file)
                self.money = n.read()
            
            elif os.path.isfile(file) is True:
                b = open(file)
                c = b.read()
                b.close()
                b = open(file ,'w+')
                v = int(c) + 500
                v = str(v)
                b.write(str(v))
                b.close()
                n = open(file)
                self.money = n.read()

    def set_level(self, file_level, file_need_xp, file_give_xp):
            if os.path.isfile(file_level) is False:
                if self.give_xp > self.need_xp:
                    self.set_need_xp(file_need_xp)
                    self.set_give_xp(file_give_xp)
                    a = open(file_level, 'w+')
                    a.write(str(self.level))
                    a.close()
                    b = open(file_level)
                    c = b.read()
                    b.close()
                    b = open(file_level  , 'w+')
                    v = int(c) + 1
                    v = str(v)
                    b.write(str(v))
                    b.close()
                    n = open(file_level)
                    self.level = n.read()
                else:
                    self.set_give_xp(file_give_xp)
                    a = open(file_level, 'w+')
                    a.write(str(self.level))
            
            elif os.path.isfile(file_level) is True:
                if self.give_xp > self.need_xp:
                    self.set_give_xp(file_give_xp)
                    self.set_need_xp(file_need_xp)
                    b = open(file_level)
                    c = b.read()
                    b.close()
                    b = open(file_level ,'w+')
                    v = int(c) + 1
                    v = str(v)
                    b.write(str(v))
                    b.close()
                    n = open(file_level)
                    self.level = n.read()
                else:
                    self.set_give_xp(file_give_xp)
                    a = open(file_level, 'w+')
                    a.write(str(file_level))

    def set_need_xp(self, file_need_xp):
        if os.path.isfile(file_need_xp) is False:
                m = open(file_need_xp, 'w+')
                m.write(str(self.need_xp))
                m.close()
                b = open(file_need_xp)
                c = b.read()
                b.close()
                b = open(file_need_xp  , 'w+')
                v = int(c) * 3
                v = str(v)
                b.write(str(v))
                b.close()
                n = open(file_need_xp)
                self.need_xp = n.read()
            
        elif os.path.isfile(file_need_xp) is True:
                b = open(file_need_xp)
                c = b.read()
                b.close()
                b = open(file_need_xp ,'w+')
                v = int(c) * 3
                v = str(v)
                b.write(str(v))
                b.close()
                n = open(file_need_xp)
                self.need_xp = n.read()


    def set_give_xp(self, file_give_xp):
            if os.path.isfile(file_give_xp) is False:
                a = open(file_give_xp, 'w+')
                a.write(str(self.give_xp))
                a.close()
                b = open(file_give_xp)
                c = b.read()
                b.close()
                b = open(file_give_xp  , 'w+')
                v = int(c) * 2
                v = str(v)
                b.write(str(v))
                b.close()
                n = open(file_give_xp)
                self.give_xp = n.read()
            
            elif os.path.isfile(file_give_xp) is True:
                b = open(file_give_xp)
                c = b.read()
                b.close()
                b = open(file_give_xp ,'w+')
                v = int(c) * 2
                v = str(v)
                b.write(str(v))
                b.close()
                n = open(file_give_xp)
                self.give_xp = n.read()    


    def take_damage(self, weapon):
            total_damage = weapon._get_damage(self.armor, 1, 0, 3, 5, 7, 9, 0.25, 0.1)

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
