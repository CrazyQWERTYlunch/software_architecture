from abc import ABC, abstractmethod
class Shape(ABC):
    """Абстрактный интерфейс фигуры"""

    @abstractmethod
    def calculate_area(self):
        """Метод расчёта площади фигуры"""
        pass

    @abstractmethod
    def calculate_perimeter(self):
        """Метод расчёта периметра фигуры"""
        pass



