# Generated by Django 3.1.4 on 2020-12-17 11:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0003_auto_20201217_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower',
            name='iin',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(1000000)]),
        ),
    ]
