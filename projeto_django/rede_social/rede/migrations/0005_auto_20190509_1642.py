# Generated by Django 2.2 on 2019-05-09 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rede', '0004_auto_20190507_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reacao',
            name='postagem',
        ),
        migrations.AddField(
            model_name='reacao',
            name='postagem',
            field=models.ManyToManyField(to='rede.Postagem'),
        ),
        migrations.AlterField(
            model_name='reacao',
            name='tipo',
            field=models.CharField(max_length=20),
        ),
    ]
