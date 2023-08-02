from IPrint import IPrint
from IData import IData

class Printer(IPrint):
    def print(self, data: IData) -> None:
        print(data.get_data())