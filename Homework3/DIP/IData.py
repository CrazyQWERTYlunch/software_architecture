from abc import ABC, abstractmethod


class IData(ABC):
    @abstractmethod
    def get_data(self):
        pass

