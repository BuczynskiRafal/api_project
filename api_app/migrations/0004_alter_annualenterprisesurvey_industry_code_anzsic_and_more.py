# Generated by Django 4.0.4 on 2022-04-12 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0003_alter_annualenterprisesurvey_variable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annualenterprisesurvey',
            name='industry_code_ANZSIC',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='annualenterprisesurvey',
            name='industry_name_ANZSIC',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='annualenterprisesurvey',
            name='rme_size_grp',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='annualenterprisesurvey',
            name='unit',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='annualenterprisesurvey',
            name='value',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='annualenterprisesurvey',
            name='variable',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
