# Generated by Django 3.1 on 2020-08-24 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0002_auto_20200824_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addition',
            name='first_number',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='addition',
            name='second_number',
            field=models.IntegerField(blank=True),
        ),
    ]
