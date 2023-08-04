from View.IShapeView import IShapeView
class CircleView(IShapeView):
    """Метод вывода на консоль площади круга"""

    def show_area(self, area: float):
        """Метод вывода площади круга"""
        print('Площадь круга равна: ' + str(area))

    def show_perimeter(self, perimeter: float):
        """Метод вывода периметра круга"""
        print('Периметр круга равен: ' + str(perimeter))

