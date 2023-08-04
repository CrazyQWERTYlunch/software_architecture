from abc import ABC,abstractmethod
class IShapeView(ABC):
    """Метод вывода на консоль площади фигуры"""

    @abstractmethod
    def show_area(area: float):
        """Метод вывода площади фигуры"""

    @abstractmethod
    def show_perimeter(perimeter: float):
        """Метод вывода периметра фигуры"""
