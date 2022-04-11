from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Load product data to the database'

    def handle(self, *args, **kwargs):
        raise NotImplementedError