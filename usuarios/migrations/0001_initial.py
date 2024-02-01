# Generated by Django 5.0.1 on 2024-02-01 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeUsuario', models.CharField(blank=True, max_length=100, null=True)),
                ('emailUsuario', models.CharField(blank=True, max_length=100, null=True)),
                ('senhaUsuario', models.CharField(blank=True, max_length=100, null=True)),
                ('descricaoCargo', models.CharField(blank=True, max_length=100, null=True)),
                ('industria', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'usuarios',
            },
        ),
    ]