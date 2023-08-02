from typing import List

class Memento:
    """Класс, фиксирующий текущее состояние"""
    def __init__(self, state: List[str]):
        self.__state = state

    def get_state(self) -> List[str]:
        return self.__state[:]


class Backpack:
    """Собираемый рюкзак"""
    def __init__(self):
        self.__state: List[str] = ['base']

    def add_a_thing(self, thing: str) -> None:
        print(f"В рюкзак положили: {thing}")
        self.__state.append(thing)

    def create_memento(self):
        return Memento(self.__state[:])

    def set_memento(self, memento: Memento):
        self.__state = memento.get_state()

    def __str__(self):
        return f"Текущее состояние рюкзака: {self.__state}"


class Student:
    def __init__(self, backpack: Backpack):
        self.backpack = backpack
        self.backpack_states: List[Memento] = []

    def add_thing_to_backpack(self, thing: str):
        self.backpack_states.append(self.backpack.create_memento())
        self.backpack.add_a_thing(thing)


    def undo_add_thing(self):
        if len(self.backpack_states) == 1:
            self.backpack.set_memento(self.backpack_states[0])
            print("Пицца вернулась в своё исходное состояние!")
            print(self.backpack)
        else:
            print("Отмена предыдущего действия")
            state = self.backpack_states.pop()
            self.backpack.set_memento(state)
            print(self.backpack)


if __name__ == "__main__":
    backpack = Backpack()
    student = Student(backpack)
    print(backpack)
    print("*" * 8 + "Добавляем вещи в рюкзак" + 8 * "*")
    student.add_thing_to_backpack('учебник')
    student.add_thing_to_backpack('ручки')
    student.add_thing_to_backpack('тетрадь')
    student.add_thing_to_backpack('сыр')
    print(backpack)
    print("*" * 4 + "Выкладываем вещи из рюкзака" + 4 * "*")
    student.undo_add_thing()
    student.undo_add_thing()
    student.undo_add_thing()
    student.undo_add_thing()
    print("*" * 8 + "Добавляем вещи в рюкзак" + 8 * "*")
    student.add_thing_to_backpack('карандаш')
    student.add_thing_to_backpack('тетрадь')
    print(backpack)