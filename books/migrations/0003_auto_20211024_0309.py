# Generated by Django 3.1.13 on 2021-10-24 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20211023_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='notes',
            field=models.TextField(blank=True, verbose_name='Notes'),
        ),
    ]
