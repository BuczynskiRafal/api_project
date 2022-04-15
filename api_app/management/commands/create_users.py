from django.core.management.base import BaseCommand
from api_app.utils import create_users


class Command(BaseCommand):

    def handle(self, *args, **options):
        n = options.get("number", 10)
        users = create_users(n)
        self.stdout.write(f"Users was created.")

    def add_arguments(self, parser):
        parser.add_argument(
            '-n',
            '--number',
            type=int,
            default=10,
            dest='number',
            help='Amount of users to create.'
        )