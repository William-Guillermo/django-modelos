# Generated by Django 4.1 on 2022-09-06 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0002_alter_clientes_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='direccion',
            field=models.CharField(max_length=50, verbose_name='La Direccion'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='tfono',
            field=models.CharField(max_length=10),
        ),
    ]
