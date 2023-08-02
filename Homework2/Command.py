from abc import ABC, abstractmethod
from typing import List


class ICommand(ABC):
    """Класс-интерфейс"""
    @abstractmethod
    def execute(self) -> None:
        ...


class Child:
    def room_cleaning(self):
        print("Ребёнок убирает комнату")

    def go_to_school(self):
        print("Ребёнок пошёл в школу")


class Father:
    def awake(self):
        print("Отец проснулся")

    def went_the_store(self):
        print("Отец отправился за хлебом")


class Mother:
    def cleaning_house(self):
        print("Мать убирает дом")

    def cooking(self):
        print("Мать готовит завтрак")


class CleaningRoom(ICommand):
    """Класс команды уборки комнаты"""
    def __init__(self, executor: Child):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.room_cleaning()


class GoToSchool(ICommand):
    def __init__(self, executor: Child):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.go_to_school()


class FatherAwake(ICommand):
    def __init__(self, executor: Father):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.awake()


class WentTheStore(ICommand):
    def __init__(self, executor: Father):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.went_the_store()

class MotherCooking(ICommand):
    def __init__(self, executor: Mother):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.cooking()

class MotherCleaning(ICommand):
    def __init__(self, executor: Mother):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.cleaning_house()

class Home:
    """Класс соединения всех команд"""
    def __init__(self):
        self.history: List[ICommand] = []

    def addCommand(self, command: ICommand) -> None:
        self.history.append(command)

    def morning(self) -> None:
        if not self.history:
            print("Семья ещё не проснулась")
        else:
            for executor in self.history:
                executor.execute()
        self.history.clear()


if __name__ == "__main__":
    child = Child()
    father = Father()
    mother = Mother()
    home = Home()
    # последовательность команд
    home.addCommand(FatherAwake(father))
    home.addCommand(WentTheStore(father))
    home.addCommand(CleaningRoom(child))
    home.addCommand(MotherCooking(mother))
    home.addCommand(GoToSchool(child))
    home.addCommand(MotherCleaning(mother))

    # запуск команд по очереди
    home.morning()
