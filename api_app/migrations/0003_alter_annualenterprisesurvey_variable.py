# Generated by Django 4.0.4 on 2022-04-12 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0002_alter_annualenterprisesurvey_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annualenterprisesurvey',
            name='variable',
            field=models.CharField(max_length=200),
        ),
    ]
