from django.core.management.base import BaseCommand
from Less_2_model_app.models import Author


class Command(BaseCommand):
    help = "Get all users."

    def handle(self, *args, **kwargs):
        author = Author.objects.all()
        self.stdout.write(f'{author}')