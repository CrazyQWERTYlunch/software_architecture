from data.in_memory_book_repository import InMemoryBookRepository
from domain.book import Book


if __name__ == "__main__":
    book1 = Book(1, "Сто лет одиночества", "Габриэль Гарсия Маркес", 755.99)
    book2 = Book(2, "Атлант расправил плечи", "Айн Рэнд", 1399)
    data_base = InMemoryBookRepository()
    data_base.add_book(book1)
    data_base.add_book(book2)
    data_base.show_all_books()
    data_base.delete_book(book2)
    data_base.show_all_books()
