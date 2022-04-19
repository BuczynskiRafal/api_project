from sqlite3 import connect
from django.test import TestCase

from .models import AnnualEnterpriseSurvey
from django.contrib.auth.models import User
from .factories import UserFactory
from .utils import csv_to_db, generate_users, create_users



class AnnualEnterpriseSurveyTestCase(TestCase):
    """Test AnnualEnterpriseSurvey class."""
    def setUp(self) -> None:
        self.connection = connect(":memory:")
        self.cursor = self.connection.cursor()

        create_table_sql = """
            CREATE TABLE test_annual_enterprise_survey
            (
                year TEXT,
                industry_code_ANZSIC TEXT,
                industry_name_ANZSIC TEXT,
                rme_size_grp TEXT,
                variable TEXT,
                value TEXT,
                unit TEXT
            );"""
        self.cursor.execute(create_table_sql)

    def test_object_create(self):
        """Object was created correctly."""
        test_annual_enterprise_survey_data = [
            (2011, 'A', 'Agriculture, Forestry and Fishing', 'a_0', 'Activity unit', '46134', 'COUNT'),
            (2011, 'A', 'Agriculture, Forestry and Fishing', 'a_0', 'Rolling mean employees', '0', 'COUNT'),
            (2011, 'A', 'Agriculture, Forestry and Fishing', 'a_0', 'Salaries and wages paid', '279', 'DOLLARS(millions)'),
        ]
        for row in test_annual_enterprise_survey_data:
            AnnualEnterpriseSurvey.objects.create(year=row[0], industry_code_ANZSIC=row[1],
                                                  industry_name_ANZSIC=row[2], rme_size_grp=row[3],
                                                  variable=row[4], value=row[5], unit=row[6])

        actual = AnnualEnterpriseSurvey.objects.last()
        expected = AnnualEnterpriseSurvey(year='2011', industry_code_ANZSIC='A',
                                          industry_name_ANZSIC='Agriculture, Forestry and Fishing', rme_size_grp='a_0',
                                          variable='Salaries and wages paid', value='279', unit='DOLLARS(millions)')
        self.assertEqual(str(actual), str(expected))

    def test_csv_to_db(self):
        csv_to_db(csv_path='test.csv', header_rows=1)
        actual = AnnualEnterpriseSurvey.objects.last()
        expected = AnnualEnterpriseSurvey(year=2011, industry_code_ANZSIC='A', industry_name_ANZSIC='Agriculture, Forestry and Fishing', rme_size_grp='a_0', variable='Salaries and wages paid', value='279', unit='DOLLARS(millions)')
        self.assertEqual(str(actual), str(expected))
        self.assertEqual(actual.year, 2011)
        self.assertEqual(actual.industry_code_ANZSIC, 'A')
        self.assertEqual(actual.industry_name_ANZSIC, 'Agriculture, Forestry and Fishing')
        self.assertEqual(actual.rme_size_grp, 'a_0')
        self.assertEqual(actual.variable, 'Salaries and wages paid')
        self.assertEqual(actual.value, '279')
        self.assertEqual(actual.unit, 'DOLLARS(millions)')

    def test_csv_to_db_error(self):
        csv_to_db(csv_path='test.csv', header_rows=1)
        actual = AnnualEnterpriseSurvey.objects.last()
        expected = AnnualEnterpriseSurvey(year=2011, industry_code_ANZSIC='A', industry_name_ANZSIC='Agriculture, Forestry and Fishing', rme_size_grp='a_0', variable='Salaries and wages paid', value='279', unit='DOLLARS(millions)')
        self.assertEqual(str(actual), str(expected))
        self.assertEqual(actual.year, 2011)
        self.assertEqual(actual.industry_code_ANZSIC, 'A')
        self.assertEqual(actual.industry_name_ANZSIC, 'Agriculture, Forestry and Fishing')
        self.assertEqual(actual.rme_size_grp, 'a_0')
        self.assertEqual(actual.variable, 'Salaries and wages paid')
        self.assertEqual(actual.value, '279')
        self.assertEqual(actual.unit, 'DOLLARS(millions)')

    def tearDown(self) -> None:
        self.connection.close()


# class CreateUsersTestCase: