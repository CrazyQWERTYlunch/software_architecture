from abc import ABC, abstractmethod
from typing import List


class SheepItem:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"овца под номером: {self.number}"


class Iterator(ABC):
    """Класс-интерфейс"""

    @abstractmethod
    def next(self) -> SheepItem:
        ...

    @abstractmethod
    def has_next(self) -> bool:
        ...


class SheepIterator(Iterator):
    def __init__(self, sheep: List[SheepItem]):
        self._sheep = sheep
        self._index = 0

    def next(self) -> SheepItem:
        sheep_item = self._sheep[self._index]
        self._index += 1
        return sheep_item

    def has_next(self) -> bool:
        return False if self._index >= len(self._sheep) else True


class SheepAggregate:
    def __init__(self, jumping_sheep: int = 20):
        self.jump_sheep = [SheepItem(it + 1) for it in range(jumping_sheep)]

    def sheep_number(self) -> int:
        return len(self.jump_sheep)

    def iterator(self) -> Iterator:
        return SheepIterator(self.jump_sheep)


if __name__ == "__main__":
    number_of_sheep = SheepAggregate(10)
    iterator = number_of_sheep.iterator()
    while iterator.has_next():
        item = iterator.next()
        print("Это " + str(item))
    print("Погрузился в сон....)")