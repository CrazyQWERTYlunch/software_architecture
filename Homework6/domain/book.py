class Book:
    """Класс объекта 'Книга'

    Атрибуты:
    - __id(int) - Индентификатор книги
    - __name(str) - Название книги
    - __author(str) - Автор книги
    - __price(float) - Цена одной книги

    Методы:
    - get_id(): int - возвращает идентификатор книги
    - get_title(): str - возвращает название книги
    - get_author(): str - возвращает автор книги
    - get_price(): float - возвращает цену за экземпляр
    - set_price(price: float) - изменяет стоимость экземпляра"""

    def __init__(self, id: int, title: str, author: str, price: float) -> None:
        """Конструктор для создания экземпляра класса
        @:param id (int): Индентификатор книги
        @:param title (str): Название книги
        @:param  author (str): Автор книги
        @:param  price (float): Цена за экземпляр
        """
        self.__id = id
        self.__title = title
        self.__author = author
        self.__price = price

    def get_id(self) -> int:
        """Возвращает идентификатор книги"""
        return self.__id

    def get_title(self) -> str:
        """Возвращает название книги"""
        return self.__title

    def get_author(self) -> str:
        """Возвращает автора книги"""
        return self.__author

    def get_price(self) -> float:
        """Возвращает цену за экземпляр книги"""
        return self.__price

    def set_price(self, price: float) -> None:
        """Устанавливает цену за 1 экземпляр книги"""
        self.__price = price

