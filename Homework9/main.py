import requests

from app import app

if __name__ == "__main__":
    app.run()
    responce = requests.get(f"http://127.0.0.1:5000/books/0")
    print(responce.json())
    responce = requests.delete(f"http://127.0.0.1:5000/books/2")
    print(responce.json())
    responce = requests.post("http://127.0.0.1:5000/books/3",
                             {"title": "Финансист", "author": "Теодор Драйзер", "price": 1200.00})
    print(responce.json())
    responce = requests.put("http://127.0.0.1:5000/books/3",
                            {"title": "Титан", "author": "Теодор Драйзер", "price": 1200.00})
    print(responce.json())
