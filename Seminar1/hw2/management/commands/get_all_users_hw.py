from django.core.management.base import BaseCommand
from hw2.models import User


class Command(BaseCommand):
    help = "Get all User."

    def handle(self, *args, **kwargs):
        user = User.objects.all()
        self.stdout.write(f'{user}')