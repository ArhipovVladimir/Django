from django.db import models


class User(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField()
    phone = models.IntegerField(max_length=11)
    adress = models.CharField(max_length=100)
    date_create = models.DateField(auto_now=True)

    def __str__(self):
        return f'Name: {self.name}, email: {self.email}, phone:{self.phone}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date_add = models.DateField(auto_now=True)

    def __str__(self):
        return f'Name: {self.name}, price: {self.price}, date_add:{self.date_add}'


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    count_product = models.IntegerField()
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'Name: {self.customer}, product: {self.products}, date_order:{self.date_ordered}'
