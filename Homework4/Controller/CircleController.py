from Controller.IShapeController import IShapeController
from View import CircleView
from Model import Circle


class CircleController(IShapeController):
    """Класс для связи расчета параметров круга и вывода их в консоль
    @:param view - поле представления объекта 'круг'
    @:param circle - поле объекта 'круг' """
    view: CircleView
    circle: Circle

    def __init__(self, view: CircleView, circle: Circle):
        """Инициализатор, создающий новый экземпляр класса CircleController с заданным объектом 'круг' и
     его представлением
     @:param view - представление объекта 'круг'
     @:param rectangle - объект 'круг' """
        self.view = view
        self.circle = circle

    def get_area(self):
        """Метод вычисления и отображения площади круга"""
        area = self.circle.calculate_area()
        self.view.show_area(area)
    def get_perimeter(self):
        """Метод вычисления и отображения периметра круга"""
        perimeter = self.circle.calculate_perimeter()
        self.view.show_perimeter(perimeter)

