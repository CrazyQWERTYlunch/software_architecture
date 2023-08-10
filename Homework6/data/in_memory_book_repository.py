from data.book_store import BookStore
from domain.book import Book


class InMemoryBookRepository(BookStore):
    """Класс реализующий функционал управления данными о книге
    Методы:
    - __init__() - Конструктор создания экземпляра класса, создает пустой список объектов типа Book
    - add_book(book: Book) - Добавляет данные о книге в список
    - delete_book(book: Book) - Удаляет данные о книге из списка
    - get_all_books(): List[Book] - Возвращает список всех книг
    """

    def __init__(self) -> None:
        """Конструктор экземпляра класса InMemoryBookRepository, создает пустой словарь объектов типа Book"""
        self.data_base: dict = {}

    def add_book(self, book: Book) -> None:
        """Добавляет данные о книге

        @:param book (Book): объект класса Book
        """
        self.data_base[book.get_id()] = [book.get_title(), book.get_author(), book.get_price()]

    def delete_book(self, book: Book) -> None:
        """Удаляет данные о книге из списка

        Args:
        @:param объект класса Book
        """
        del self.data_base[book.get_id()]

    def show_all_books(self):
        """Демонстрирует полный список книг и их данные"""
        for i in self.data_base.keys():
            print(i, *self.data_base[i], sep=". ")
