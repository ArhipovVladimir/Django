from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    adress = models.CharField(max_length=100)
    date_create = models.DateField(auto_now=True)

    def __str__(self):
        return f'Name: {self.name}, email: {self.email}, phone:{self.phone}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date_add = models.DateField(auto_now=True)
    quantity = models.IntegerField()

    def __str__(self):
        return f'Name: {self.name}, price: {self.price}, quantity: {self.quantity} date_add:{self.date_add}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    count_products = models.IntegerField()
    date_order = models.DateField()
    # date_order = models.DateField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'Name: {self.client}, date_order:{self.date_order}, total_price:{self.total_price}'

