class Product:
    """ * Класс Product представляет товар, который может быть добавлен в заказ.
        * Этот класс содержит информацию о товаре, такую как идентификатор, название, стоимость и количество.
    """

    def __init__(self, id: int, name: str, price: float, count: int):
        """
        Инициализирует объект Product.

        Аргументы:
            @:param id (int): Идентификатор товара.
            @:param name (str): Название товара.
            @:param price (float): Стоимость товара.
            @:param count (int): Количество товара.
        """
        self.id = id
        self.name = name
        self.price = price
        self.count = count

    def __str__(self) -> str:
        """
        Cтроковое представление товара.
        """
        return f"id = {self.id}, название = '{self.name}', цена = {self.price}, количество = {self.count}"

    def __hash__(self) -> int:
        """
        Возвращает хэш-код товара.

        """
        return hash((self.id, self.name, self.price, self.count))

    def __eq__(self, other) -> bool:
        """
        Проводит сравнение товара

        Аргументы:
            @:param other (Product): Другой товар для сравнения.
        """
        if isinstance(other, Product):
            return (self.id, self.name, self.price, self.count) == (other.id, other.name, other.price, self.count)
        return False
