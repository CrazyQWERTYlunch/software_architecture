from cached_order_repository import CachedOrderRepository
from product import Product
from order import Order
from order_item import OrderItem

product_store = CachedOrderRepository('shop.db')

product_1 = Product(id=1, name='Атлант расправил плечи', price=799.99, count=100)
product_2 = Product(id=2, name='Удивительная история Билли Миллигана', price=372.00, count=500)
product_3 = Product(id=3, name='Цветы для Элджернона', price=500.99, count=250)
product_store.add_product(product_1)
product_store.add_product(product_2)

order_1 = Order()

order_item_1 = OrderItem(product=product_1, quantity=5)
order_item_2 = OrderItem(product=product_2, quantity=8)

product_store.save(order=order_1, order_items=[order_item_1, order_item_2])

product_store.get_last_order()
