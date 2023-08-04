from View.IShapeView import IShapeView
class RectangleView(IShapeView):
    """Метод вывода на консоль площади прямоугольника"""

    def show_area(self, area: float):
        """Метод вывода площади прямоугольника"""
        print('Площадь прямоугольника равна: ' + str(area))

    def show_perimeter(self, perimeter: float):
        """Метод вывода периметра прямоугольника"""
        print('Периметр прямоугольника равен: ' + str(perimeter))

