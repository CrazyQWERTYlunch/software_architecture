from math import sqrt

from Model.Shape import Shape


class Triangle(Shape):
    """Класс фигуры 'треугольник', наследник интерфейса 'Shape'"""

    def __init__(self, side1=0.00, side2=0.00,side3=0):
        """Метод инициализатор объекта класса
            @:param side1 длина первой стороны треугольника (базовое значение = 0) (должен быть положительным числом)
            @:param side2 длина второй стороны треугольника (базовое значение = 0) (должен быть положительным числом)
            @:param side3 длина третьей стороны треугольника (базовое значение = 0) (должен быть положительным числом)
            @:raise ValueError - (Нельзя вводить числа <= 0) """

        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ValueError('Ширина и длина прямоугольника не может быть меньше или равна 0')
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        """Метод расчёта площади треугольника
            @:return площадь треугольника (тип float)"""
        s = (self.side1 + self.side2 + self.side3) / 2
        return sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def calculate_perimeter(self):
        """Метод расчёта периметра треугольника
            @:return периметр треугольника (тип float)"""

        return self.side1 + self.side2 + self.side3

