from django.core.management.base import BaseCommand
from Less_2_model_app.models import Author


class Command(BaseCommand):
    help = "Delete all author."

    def handle(self, *args, **kwargs):

        author = Author.objects.all()
        if author is not None:
            author.delete()
            self.stdout.write(f'{author}')