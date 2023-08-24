from flask import Flask
from flask_restful import Api, Resource, reqparse

from book import Book
from in_memory_book_repository import InMemoryBookRepository

app = Flask(__name__)
# Взаимодействие с restful
api = Api()

book1 = Book(1, "Сто лет одиночества", "Габриэль Гарсия Маркес", 755.99)
book2 = Book(2, "Атлант расправил плечи", "Айн Рэнд", 1399)
data_base = {book1.get_id(): {"title": book1.get_title(), "author": book1.get_author(),
                                         "price": book1.get_price()},
             book2.get_id():{"title": book2.get_title(), "author": book2.get_author(),
                                         "price": book2.get_price()}}

class Controller(Resource):
    def get(self, book_id):
        if book_id == 0:
            return data_base
        return data_base[book_id]

    def delete(self, book_id):
        del data_base[book_id]
        return data_base

    # Реализует изменение и добавление книги метод post и put
    def post(self, book_id):
        parser = reqparse.RequestParser()
        parser.add_argument("title", type=str)
        parser.add_argument("author", type=str)
        parser.add_argument("price", type=float)
        data_base[book_id] = parser.parse_args()
        return data_base


# Обработка URL фадреса
api.add_resource(Controller, "/books/<int:book_id>")
api.init_app(app)
