# Generated by Django 2.2 on 2019-05-24 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0003_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(choices=[('S', 'sim'), ('N', 'não'), ('NSO', 'não soube opinar')], default='NSO', max_length=3, null=True),
        ),
    ]
