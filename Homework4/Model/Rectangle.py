from Model.Shape import Shape


class Rectangle(Shape):
    """Класс фигуры 'прямоугольник', наследник интерфейса 'Shape'"""

    def __init__(self, length=0.00, width=0.00):
        """Метод инициализатор объекта класса
            @:param lenght длина прямоугольника (базовое значение = 0) (должен быть положительным числом)
            @:param width ширина прямоугольника (базовое значение = 0) (должен быть положительным числом)
            @:raise ValueError - (Нельзя вводить числа <= 0) """

        if length <= 0 or width <= 0:
            raise ValueError('Ширина и длина прямоугольника не может быть меньше или равна 0')
        self.length = length
        self.width = width

    def calculate_area(self):
        """Метод расчёта площади прямоугольника
            @:return площадь прямоугольника (тип float)"""

        return self.length * self.width

    def calculate_perimeter(self):
        """Метод расчёта периметра прямоугольника
            @:return периметр прямоугольника (тип float)"""

        return 2 * (self.length + self.width)
