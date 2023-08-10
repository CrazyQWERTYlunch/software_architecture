from abc import ABC, abstractmethod


class BookStore(ABC):
    """Абстрактный класс для работы с данными о книге"""

    @abstractmethod
    def add_book(self):
        """Сохраняет книгу и её данные"""

    @abstractmethod
    def delete_book(self):
        """Удаляет книгу и данные о ней"""

    @abstractmethod
    def show_all_books(self):
        """Демонстрирует полный список книг и их данные"""
