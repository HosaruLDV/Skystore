# Generated by Django 4.1.5 on 2023-01-26 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbl', '0008_alter_blog_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('True', 'положительный'), ('False', 'отрицательный')], default='True', max_length=15),
        ),
    ]
