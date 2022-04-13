import os
from django.core.management.base import BaseCommand
from api_app.utils import csv_to_db


class Command(BaseCommand):
    help = "Insert data from csv to db"
    csv_path = os.path.join("annual-enterprise-survey-2020-financial-year-provisional-size-bands-csv.csv")

    def handle(self, *args, **options):
        csv_path = options.get("csv_path", os.path.join("annual-enterprise-survey-2020-financial-year-provisional-size-bands-csv.csv"))
        header_rows = options.get("header_rows", 1)
        csv_to_db(csv_path=csv_path, header_rows=header_rows)
        self.stdout.write(f"Data was added.")

    def add_arguments(self, parser):
        parser.add_argument(
            '-rows',
            '--header_rows',
            type=int,
            default=10,
            dest='header_rows',
            help='Count of header rows.'
        )
        parser.add_argument(
            '-path',
            '--csv_path',
            type=str,
            default=os.path.join("annual-enterprise-survey-2020-financial-year-provisional-size-bands-csv.csv"),
            dest='csv_path',
            help='A path to csv file containing data to insert to database.'
        )
