# Generated by Django 2.2 on 2019-04-30 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_auto_20190429_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='blog',
            field=models.ForeignKey(on_delete='DO_NOTHING', to='myapp.Blog'),
        ),
    ]
