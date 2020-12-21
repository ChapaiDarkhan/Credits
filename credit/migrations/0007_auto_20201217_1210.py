# Generated by Django 3.1.4 on 2020-12-17 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0006_blacklist_iin'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blacklist',
            options={'verbose_name': 'Credit', 'verbose_name_plural': 'Blacklist'},
        ),
        migrations.RemoveField(
            model_name='blacklist',
            name='black_book',
        ),
        migrations.AlterField(
            model_name='program',
            name='age_max',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='program',
            name='age_min',
            field=models.IntegerField(),
        ),
    ]
