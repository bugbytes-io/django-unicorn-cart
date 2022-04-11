from django.core.management.base import BaseCommand
from core.models import Product


class Command(BaseCommand):
    help = 'Load product data to the database'

    def handle(self, *args, **kwargs):
        Product.objects.get_or_create(
            name='Pizza',
            price=5.50
        )
        Product.objects.get_or_create(
            name='Peppers',
            price=2.50
        )
        Product.objects.get_or_create(
            name='Bread',
            price=2.00
        )
        Product.objects.get_or_create(
            name='Quinoa',
            price=15.50
        )
        Product.objects.get_or_create(
            name='Rice',
            price=8.25
        )