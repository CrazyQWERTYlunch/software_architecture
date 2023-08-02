from abc import ABC, abstractmethod
from IData import IData


class IPrint(ABC):
    @abstractmethod
    def print(self, data: IData) -> None:
        pass
