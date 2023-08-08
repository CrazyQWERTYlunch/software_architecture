class Person:
    """Класс, представляющий пользователя

         Атрибуты:
         - _first_name (str): имя пользователя
         - _last_name(str): фамилия польователя
         - _age (int): возраст пользователя
         """
    def __init__(self, first_name, last_name, age):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age

    @property
    def get_name(self):
        # возвращает имя пользователя
        return self._first_name
    @property
    def get_last_name(self):
        # возвращает фамилию пользователя
        return self._last_name
    @property
        # возвращает возраст пользователя
    def get_age(self):
        return self._age

