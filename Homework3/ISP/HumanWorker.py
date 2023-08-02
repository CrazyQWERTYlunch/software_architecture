from IEating import IEating
from IWorker import IWorking


class HumanWorker(IEating, IWorking):
    def work(self) -> None:
        print('Человек работает')

    def eat(self) -> None:
        print('Человек ест')