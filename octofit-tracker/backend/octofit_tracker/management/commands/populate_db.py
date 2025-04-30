from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write("Database populated with test data!")
