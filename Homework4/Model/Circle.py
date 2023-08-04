from Model.Shape import Shape
from math import pi


class Circle(Shape):
    """Класс фигуры 'круг', наследник интерфейса 'Shape'"""

    def __init__(self, radius=0.00):
        """Метод инициализатор объекта класса круг
            @:param radius - радиус круга (базовое значение = 0) (должен быть положительным числом)
            @:raise ValueError - (Нельзя вводить числа <= 0) """

        if radius <= 0:
            raise ValueError('Радиус не может быть меньше или равен 0')
        self.radius = radius

    def calculate_area(self):
        """Метод расчёта площади круга
            @:return площадь круга (тип float)"""

        return pi * self.radius ** 2

    def calculate_perimeter(self):
        """Метод расчёта периметра круга
            @:return периметр круга (тип float)"""

        return 2 * pi * self.radius
