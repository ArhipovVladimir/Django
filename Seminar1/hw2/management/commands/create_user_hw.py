from django.core.management.base import BaseCommand
from hw2.models import User


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        # user = User(name='Vladimir', email='capitan@example.com', phone=1234567891, adress='adress')
        user = User(name='Vladimir1', email='arh@example.com', phone=1234567891, adress='adress')

        user.save()
        self.stdout.write(f'{user}')

