from Controller.IShapeController import IShapeController
from View import RectangleView
from Model import Rectangle
class RectangleController(IShapeController):
    """Класс для связи расчета параметров прямоугольника и вывода их в консоль
    @:param view - поле представления объекта 'прямоугольник'
    @:param rectangle - поле объекта 'прямоугольник' """
    view: RectangleView
    rectangle: Rectangle

    def __init__(self, view: RectangleView, rectangle: Rectangle):
        """Инициализатор, создающий новый экземпляр класса RectangleController с заданным объектом 'прямоугольник' и
     его представлением
     @:param view - представление объекта 'прямоугольник'
     @:param rectangle - объект 'прямоугольник' """
        self.view = view
        self.rectangle = rectangle

    def get_area(self):
        """Метод вычисления и отображения площади прямоугольника"""
        area = self.rectangle.calculate_area()
        self.view.show_area(area)
    def get_perimeter(self):
        """Метод вычисления и отображения периметра прямоугольника"""
        perimeter = self.rectangle.calculate_perimeter()
        self.view.show_perimeter(perimeter)

