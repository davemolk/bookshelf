# Generated by Django 3.1.13 on 2021-10-24 10:44

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
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Record Title')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True, verbose_name='Record Slug')),
                ('notes', models.TextField(blank=True, verbose_name='Notes')),
                ('record_url', models.URLField(blank=True, verbose_name='URL')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
