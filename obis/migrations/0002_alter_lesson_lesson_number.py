# Generated by Django 5.0 on 2023-12-09 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='lesson_number',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
