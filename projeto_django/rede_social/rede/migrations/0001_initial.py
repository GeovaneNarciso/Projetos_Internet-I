# Generated by Django 2.2 on 2019-05-07 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('contatos', models.ManyToManyField(related_name='_perfil_contatos_+', to='rede.Perfil')),
            ],
            options={
                'verbose_name_plural': 'Perfil',
            },
        ),
        migrations.CreateModel(
            name='Postagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=255)),
                ('data', models.DateField()),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rede.Perfil')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('senha', models.CharField(max_length=20)),
                ('dt_nasc', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Reacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('peso', models.IntegerField()),
                ('tipo', models.CharField(choices=[('C', 'curtir'), ('A', 'amar'), ('R', 'rir'), ('I', 'se impressionar'), ('T', 'ficar triste'), ('B', 'ficar bravo')], max_length=1, null=True)),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rede.Perfil')),
                ('postagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rede.Postagem')),
            ],
        ),
        migrations.AddField(
            model_name='perfil',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rede.Usuario'),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=255)),
                ('data', models.DateField()),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rede.Perfil')),
                ('postagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rede.Postagem')),
            ],
        ),
    ]
