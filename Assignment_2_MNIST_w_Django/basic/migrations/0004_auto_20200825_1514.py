# Generated by Django 3.1 on 2020-08-25 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0003_auto_20200824_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addition',
            name='result',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]