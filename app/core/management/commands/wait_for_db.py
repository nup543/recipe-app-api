
"""

can run this as python manage.py command
DJANGO command to wait for db to be available
"""

from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        pass