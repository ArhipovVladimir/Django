import datetime

from django.core.management import BaseCommand
from random import randint, choice, choices
from hw3.models import Product, Client, Order

class Command(BaseCommand):
    help = 'Create fake data in store'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
       count = kwargs.get('count')
       products = ['bread', 'butter', 'milk', 'fish', 'meat', 'water', 'apple', 'banana', 'bagel', 'orange']

       for i in range(count + 1):
            product = Product(name=f'Product_{i+1}', description=f'{choice(products)}',
                              price=randint(50, 500), quantity=randint(1, 3))
            product.save()

       cities = ['Tomsk', 'Moscow', 'New_York', 'Novosibirsk', 'Kathmandu']
       for i in range(count + 1):
            client = Client(name=f'Client_{i + 1}', email=f'client_{i + 1}@mail.ru', phone=f'+790000000{i}{i}',
                            adress=f'{choice(cities)}')
            client.save()

       products = [*Product.objects.all()]

       for client in Client.objects.all():
            # кол-во заказов у клиента от 1 до 5
            for _ in range(randint(1, 6)):
                order = Order(client=client, count_products=randint(1, 10), total_price=randint(1, 10),
                              date_order=f'{randint(2022, 2023)}-{randint(1, 12)}-{randint(1, 28)}')
                order.save()
                order_sum = 0
                # кол-во товаров в заказе от 1 до 5
                order_products = choices(products, k=randint(1, 5))

                for product in order_products:
                    # сумма товаров в заказе
                    order_sum += product.price

                # ManyToManyField заполняется после записи order
                # добавляем продукты в заказ
                order.products.set(order_products)
                order.sum_order = order_sum
                order.save()