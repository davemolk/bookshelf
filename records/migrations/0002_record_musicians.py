# Generated by Django 3.1.13 on 2021-10-26 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='musicians',
            field=models.TextField(blank=True, verbose_name='Musicians'),
        ),
    ]