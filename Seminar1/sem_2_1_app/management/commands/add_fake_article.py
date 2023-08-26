from django.core.management.base import BaseCommand
# from sem_2_1_app.models import Author, Post
# from Seminar1.sem_2_1_app.models import Author
from datetime import datetime
from sem_2_1_app.models import Article, Author
from random import randint

class Command(BaseCommand):
    help = "Generate fake authors and posts."

    def handle(self, *args, **kwargs):
       for author in Author.objects.all():
            for i in range(3):
                article = Article(head=f'Head{i}',
                                  content=f'Contene{i}',
                                  author=author,
                                  category=f'category {i}',
                                  public=randint(0, 1)
                                                            )
                article.save()
       self.stdout.write(f'create article')

