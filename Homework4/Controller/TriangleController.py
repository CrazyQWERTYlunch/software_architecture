from Controller.IShapeController import IShapeController
from View import TriangleView
from Model import Triangle

class TriangleController(IShapeController):
    """Класс для связи расчета параметров треугольника и вывода их в консоль
    @:param view - поле представления объекта 'треугольник'
    @:param rectangle - поле объекта 'треугольник' """
    view: TriangleView
    triangle: Triangle

    def __init__(self, view: TriangleView, triangle: Triangle):
        """Инициализатор, создающий новый экземпляр класса TriangleController с заданным объектом 'треугольник' и
     его представлением
     @:param view - представление объекта 'треугольник'
     @:param triangle - объект 'треугольник' """
        self.view = view
        self.triangle = triangle

    def get_area(self):
        """Метод вычисления и отображения площади треугольникa"""
        area = self.triangle.calculate_area()
        self.view.show_area(area)

    def get_perimeter(self):
        """Метод вычисления и отображения периметра треугольникa"""
        perimeter = self.triangle.calculate_perimeter()
        self.view.show_perimeter(perimeter)
