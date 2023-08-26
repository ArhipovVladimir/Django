from django.db import models
from datetime import datetime
from random import randint


class Kicks(models.Model):
    result = models.BooleanField()
    kick_time = models.DateTimeField(auto_now_add=datetime.now())

    def __str__(self):
        return f'Username: {self.result} kick_time: {self.kick_time}'

    @staticmethod
    def statistics(n: int):
        reshka = 0
        orel = 0
        for _ in range(n):
            kick = Kicks(result=randint)
            if kick.result:
                reshka += 1
            orel += 1

        result_dict = {
            'орел': reshka,
            'решка': orel
        }
        return result_dict


class Author(models.Model):
        name = models.CharField(max_length=100)
        surname = models.CharField(max_length=100)
        email = models.EmailField()
        biography = models.TextField()
        birthday = models.DateTimeField(auto_now=True)

        def __str__(self):
            return f'Fullname: {self.name} {self.surname} email: {self.email} birthday:'


class Article(models.Model):
        head = models.CharField(max_length=100)
        content = models.TextField()
        date = models.DateField(auto_now=True)
        author = models.ForeignKey(Author, on_delete=models.CASCADE)
        category = models.CharField(max_length=100)
        count = models.IntegerField(default=0)
        public = models.BooleanField(default=False)

        def __str__(self):
            return f'Title is {self.head}, count view {self.count}'


