from django.core.management.base import BaseCommand
from hw2.models import Order, User, Product


class Command(BaseCommand):
    help = "Get all oreder by User id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = User.objects.filter(pk=pk).first()
        if user is not None:
            orders = Order.objects.filter(user=user)
            intro = f'All orsers of {user.name}\n'
            text = '\n'.join(order.prouct.name for order in orders)
            self.stdout.write(f'{intro}{text}')
