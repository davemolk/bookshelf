# Generated by Django 3.1.13 on 2021-10-22 17:04

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Book Title')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True, verbose_name='Book Slug')),
                ('author', models.CharField(blank=True, max_length=255)),
                ('notes', models.TextField(blank=True, verbose_name='Description')),
                ('cover', models.ImageField(blank=True, upload_to='covers/')),
                ('url', models.URLField(blank=True, verbose_name='URL')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]