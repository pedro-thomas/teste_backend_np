# Generated by Django 5.0.1 on 2024-02-01 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitoramento_ambiental', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='analiseautomatica',
            table='analiseAutomatica',
        ),
        migrations.AlterModelTable(
            name='produtor',
            table='produtores',
        ),
        migrations.AlterModelTable(
            name='propriedade',
            table='propriedades',
        ),
        migrations.AlterModelTable(
            name='vinculo',
            table='vinculos',
        ),
    ]
