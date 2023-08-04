from View.IShapeView import IShapeView
class TriangleView(IShapeView):
    """Метод вывода на консоль площади треугольника"""

    def show_area(self, area: float):
        """Метод вывода площади треугольника"""
        print('Площадь треугольника равна: ' + str(area))

    def show_perimeter(self, perimeter: float):
        """Метод вывода периметра треугольника"""
        print('Периметр треугольника равен: ' + str(perimeter))

