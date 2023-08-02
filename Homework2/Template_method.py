from abc import ABC, abstractmethod
from typing import List

class Salad:
    """Класс приготовляемого салата"""
    def __init__(self):
        self.__state: List[str] = []

    def add_ingredient(self, ingredient: str) -> None:
        print(f"В салат добавили: {ingredient}")
        self.__state.append(ingredient)

    def __str__(self):
        return f"Ингридиенты салата: {self.__state}"


class SaladMaker(ABC):
    """Базовый класс шаблонного метода"""
    def make_salad(self, salad: Salad) -> None:
        self.prepare_sauce(salad)
        self.prepare_topping(salad)
        self.cook(salad)

    @abstractmethod
    def prepare_sauce(self, salad: Salad) -> None:
        ...

    @abstractmethod
    def prepare_topping(self, salad: Salad) -> None:
        ...

    @abstractmethod
    def cook(self, salad: Salad) -> None:
        ...


class CaesarMaker(SaladMaker):
    """Класс приготовления салата Цезарь"""
    def prepare_sauce(self, salad: Salad) -> None:
        salad.add_ingredient('Olive oil')

    def prepare_topping(self, salad: Salad) -> None:
        salad.add_ingredient('lettuce leaves')
        salad.add_ingredient('tomato')
        salad.add_ingredient('chicken')
        salad.add_ingredient('parmesan')

    def cook(self, salad: Salad) -> None:
        print("Салат 'Цезарь' готов")

class Chief:
    """Класс повара"""
    def __init__(self, template_salad: SaladMaker):
        self.__cook = template_salad

    def set_cook_template(self, template_salad: SaladMaker):
        self.__cook = template_salad

    def make_salad(self) -> Salad:
        salad = Salad()
        self.__cook.make_salad(salad)
        return salad


if __name__ == "__main__":
    chief = Chief(CaesarMaker())
    print("*"*8 + "Готовим салат 'Цезарь'"+8*"*")
    print(chief.make_salad())
