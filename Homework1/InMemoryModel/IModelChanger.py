from abc import ABC,abstractmethod

class IModelChanger(ABC):
    @abstractmethod
    def notify_change(ModelChanger: sender):
        pass