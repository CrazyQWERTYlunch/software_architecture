from abc import ABC, abstractmethod

class IWorker(ABC):
    """Абстрактный класс обработчика"""
    @abstractmethod
    def set_next_worker(self, worker : 'IWorker') -> 'IWorker':
        pass

    @abstractmethod
    def execute(self,  command: str) -> str:
        pass

class AbsWorker(IWorker):
    """Абстрактный класс, наследуемый от интерфейса"""
    def __init__(self):
        self.__next_worker: IWorker = None

    def set_next_worker(self, worker: 'IWorker') -> 'IWorker':
        self.__next_worker = worker
        return worker

    def execute(self,  command: str) -> str:
        if self.__next_worker is not None:
            return self.__next_worker.execute(command)

class Director(AbsWorker):
    def execute(self,  command: str) -> str:
        if command == 'контроль организации':
            return 'Директор выполнил задачу: ' + command
        return super().execute(command) # Передача команды следующему в цепочке

class HeadTeacher(AbsWorker):
    def execute(self,  command: str) -> str:
        if command == 'организация учебного процесса':
            return 'Зав.уч выполнил задачу: ' + command
        return super().execute(command)
class Teacher(AbsWorker):
    def execute(self,  command: str) -> str:
        if command == 'планирование учебного материала по своему предмету':
            return 'Учитель выполнил задачу: ' + command
        return super().execute(command)


def give_command(worker: IWorker, command: str):
    string: str = worker.execute(command)
    if string == '':
        print(command + '- никто не выполнил данную задачу')
    else:
        print(string)

if __name__ == '__main__':
    director = Director()
    head_teacher = HeadTeacher()
    teacher = Teacher()

    director.set_next_worker(head_teacher).set_next_worker(teacher)
    give_command(director, 'контроль организации')
    give_command(director, 'организация учебного процесса')
    give_command(director, 'планирование учебного материала по своему предмету')
    give_command(director, 'ремонт холодильника')

