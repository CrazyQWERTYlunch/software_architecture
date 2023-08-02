from IWorker import IWorking

class RobotWorker(IWorking):
    def work(self) -> None:
        print('Робот работает')
