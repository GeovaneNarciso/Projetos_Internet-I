# Generated by Django 2.2 on 2019-04-12 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='city',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
