from django.core.management.base import BaseCommand
from hw2.models import Order


class Command(BaseCommand):
    help = "Get Oder with date  <date>."

    def add_arguments(self, parser):
        parser.add_argument('date_ordered', type=int, help='Date Order')

    def handle(self, *args, **kwargs):
        date_ordered = kwargs['date_ordered']
        order = Order.objects.filter(date_ordered__gt=date_ordered)
        self.stdout.write(f'{order}')