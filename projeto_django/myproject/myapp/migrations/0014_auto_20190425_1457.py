# Generated by Django 2.2 on 2019-04-25 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20190423_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
