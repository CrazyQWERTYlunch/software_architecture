from abc import ABC, abstractmethod

class IShapeController(ABC):
    """Интерфейс для связи расчета параметров геометрической фигуры и вывода их в консоль"""

    @abstractmethod
    def get_area(self):
        """Метод расчёта площади фигуры и вывода её в консоль"""

    @abstractmethod
    def get_perimeter(self):
        """Метод расчета периметра геометрической фигуры и вывода ее в консоль"""
