import os
import csv
import sqlite3
import datetime
import colorama
from pathlib import Path
from .factories import UserFactory
from threading import Thread

from .models import AnnualEnterpriseSurvey, User
from .factories import UserFactory

# BASE_DIR = Path(__file__).resolve().parent.parent


def csv_to_db(csv_path, header_rows):
    """Create data in annual_enterprise_survey_2020 table from csv file."""

    with open(csv_path) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            try:
                created = AnnualEnterpriseSurvey.objects.get_or_create(
                    year=row[0],
                    industry_code_ANZSIC=row[1],
                    industry_name_ANZSIC=row[2],
                    rme_size_grp=row[3],
                    variable=row[4],
                    value=row[5],
                    unit=row[6],
                )
            except (ValueError, TypeError) as e:
                with open('error_data', 'a', encoding='utf-8') as error_file:
                    error_file.write(str(row) + '\n')


# def create_users(n=1000):
#     """Create users"""
#     for _ in range(n):
#         user = UserFactory()
#         user.save()


def generate_users(n):
    """Generate users"""
    for _ in range(n):
        print(colorama.Fore.BLUE + '-- starting generate user')
        user = UserFactory()
        print(colorama.Fore.YELLOW + '++ user has been created')
        user.save()
        print(colorama.Fore.GREEN + '** user was saved')


def create_users(n=100):

    """Create threads"""
    threads = [Thread(target=generate_users, args=(n,)) for _ in range(5)]

    """t0 - will be used to calculate how long the function work"""
    t0 = datetime.datetime.now()

    """Starting threads"""
    [t.start() for t in threads]

    """Wait till all threads finish work."""
    [t.join() for t in threads]

    dt = datetime.datetime.now() - t0
    print(colorama.Fore.GREEN + f"Working time: {dt.total_seconds():,.2f} sec.")

