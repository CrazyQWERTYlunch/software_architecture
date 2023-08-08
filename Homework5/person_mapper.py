from person import Person


class PersonMapper():
    f"""Класс, представляющий конвертер информации пользователей

        Атрибуты:
        - number (int): идентификатор пользователей
        - __mapping (dict) - хранилище пользователей (псевдо БД)

        Методы:

        - add_data(person: Person) - Добавляет пользователя
        - find_by_id(user_id: int): User - Ищет пользователя по Id
        - show_dictionary(): - Демонстрирует все имеющиеся записи в БД
        - delete_person(person: Person) - Удаляет пользователя
        - to_person() - Превращает пользователя в объект класса Person"""

    number = 1
    def __init__(self):
        self.__mapping = {}

    def add_data(self, person: Person):
        # Метод, реализующий добавление пользователей в БД
        self.__mapping[self.number] = [person.name, person.last_name, person.age]
        self.number += 1

    def find_by_id(self, id):
        # Метод, реализующий поиск в словаре по id
        if self.__mapping[id]:
            return self.__mapping[id]
        raise Exception(f"Пользователь с id {id} не найден")

    def show_dictionary(self):
        # Метод, который демонстрирует всё наполнение БД
        print(self.__mapping)

    def delete_person(self, id):
        # Метод, удаляющий человека из словаря
        del self.__mapping[id]

    def to_person(self, id):
        # Метод, который преобразует данные из словаря mapping в объект Person
        person = Person(self.__mapping[id][0], self.__mapping[id][1], self.__mapping[id][2])
        return person
