class Person:
    def __init__(self, name:str, age:int, iq:int, height:int, weight:int):
        self.age = age
        self.iq = iq
        self.height = height
        self.weight = weight
        self.name = name

    def info(self):
        return f'{self.name}\nВозраст:{self.age}\nАйкью:{self.iq}'  


class Tester:
    def __init__(self, age:int, iq:int):
        self.age = age
        self.iq = iq
        self.best = ['', 0]

    def selection(self, value:Person):
        if self.age <= value.age and self.iq <= value.iq:
            if value.iq > self.best[1]:
                self.best[0] = value.name
                self.best[1] = value.iq
            return True
        else:
            return False
        
    def best_person(self):
        return self.best[0]
      

        


if __name__ == "__main__":
    tester = Tester(16, 100)

    m = [
        Person("Анатолий", 21, 110, 178, 79),
        Person("Арина", 14, 100, 175, 45),
        Person("Ася", 15, 105, 173, 47),
        Person("Антон", 20, 111, 172, 78)
    ]

    for person in m:
        if tester.selection(person):
         print(person.info())
    print("Человек с самым высоким айкью:", tester.best_person())
        

