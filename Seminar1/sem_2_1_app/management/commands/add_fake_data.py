from django.core.management.base import BaseCommand
# from sem_2_1_app.models import Author, Post
# from Seminar1prog.sem_2_1_app.models import Author
from datetime import datetime
from sem_2_1_app.models import Author


class Command(BaseCommand):
    help = "Generate fake authors and posts."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(name=f'Name{i}', surname=f'Surame{i}', email=f'mail{i}@mail.ru',
                            biography='bla_bla_bla')
            author.save()
        self.stdout.write(f'create {count} Author')
