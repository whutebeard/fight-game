from math import pi
from math import sin
from math import sqrt

class Shape:
    def get_perimetr(self) -> float:
       return 0
    
    def get_S(self) -> float:
        return 0

class Circle(Shape):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError('Радиус должен быть положительным числом!')
        super().__init__()
        self.radius = radius

    def get_perimetr(self) -> float:
        return 2 * pi *self.radius
    
    def get_S(self) -> float:
        return 2 * pi * self.radius ** 2

    
    
class Rectangle(Shape):
    def __init__(self, lenght: float, width:float) -> float:
        if lenght <= 0 or width <= 0:
            raise ValueError('Длина и ширина должны быть положительным!')

        super().__init__()
        self.lenght = lenght
        self.width = width

    def get_perimetr(self) -> float:
        return 2 * self.lenght + 2 * self.width
    
    def get_S(self) -> float:
        return self.lenght * self.width
    
  
class Triangle(Shape):
    def __init__(self, edges: tuple[float, float, float]) -> float:
        if edges[0] + edges[1] <= edges[2] or edges[1] + edges[2] <= edges[0] or edges[2] + edges[0] <= edges[1]:
            raise ValueError('Неправильно заданы стороны!')
        super().__init__()
        self.edges = edges

    def get_perimetr(self) -> float:
        return sum(self.edges)
    
    def get_S(self) -> float:
        return self.edges[0] ** 2 * self.edges[1] / sqrt(self.edges[0] ** 2 * 4 + self.edges[1] ** 2 * 4)


class Square(Rectangle):
    def __init__(self, lenght: float) -> float:
        super().__init__(lenght = lenght, width = lenght)
    
class RegularTriangle(Triangle):
    def __init__(self, side: float) -> float:
        super().__init__([side, side, side])
    


if __name__ == '__main__':
    circle = Circle(10)
    print(circle.get_perimetr())
    print(circle.get_S())
    square = Square(10)
    print(square.get_perimetr())
    print(square.get_S())
    regulartriangle = RegularTriangle(10)
    print(regulartriangle.get_perimetr())
    print(regulartriangle.get_S())
    rectangle = Rectangle(10, 5)
    print(rectangle.get_perimetr())
    print(rectangle.get_S())
    triangle = Triangle([5, 10, 6])
    print(triangle.get_perimetr())
    print(triangle.get_S())
