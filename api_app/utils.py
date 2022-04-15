import os
import csv
import sqlite3
from pathlib import Path
from .factories import UserFactory

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


def create_users(n=1000):
    """Create users"""
    for _ in range(n):
        user = UserFactory()
        user.save()

