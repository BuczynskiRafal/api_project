import os
import csv
import sqlite3
from pathlib import Path

from .models import AnnualEnterpriseSurvey


# BASE_DIR = Path(__file__).resolve().parent.parent

def csv_to_db(csv_path, header_rows):
    """Create data in annual_enterprise_survey_2020 table from csv file."""

    with open(csv_path) as csv_file:
        reader = csv.reader(csv_file)
        counter = 0
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



# dopisać obsługę wyjątków - błędne dane zapisywane do nowego pliku
# dopisac testy do csv_to_db - zrobione
# test sprawdzający czy rekord dodał się do bazy - zrobione na orm django
# sprawdizć coverage utils.py - sprawdzono
# dopracować pobieranie danych bez nagłówka - pomysleć jak uogólnić
# (przyjmowanie pliku jako argument i ilść wierszy nagłówka jakie trzeba opuścić jako argument) - zrobione
# testowanie wielowątkowości - symulowanie ludzi którzy chcą się zapisac do bazy - wiele wątków
