# Generated by Django 2.2 on 2019-05-03 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_auto_20190430_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Blog'),
        ),
    ]