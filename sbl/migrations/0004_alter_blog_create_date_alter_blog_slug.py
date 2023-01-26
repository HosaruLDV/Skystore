# Generated by Django 4.1.5 on 2023-01-26 19:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbl', '0003_alter_blog_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2023, 1, 26, 19, 18, 49, 160319, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(max_length=250, unique=True, verbose_name='slug'),
        ),
    ]