# Generated by Django 4.1.2 on 2022-10-07 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0003_articulo_almacen_cantidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo_almacen',
            name='cantidad',
            field=models.BigIntegerField(default=1),
        ),
    ]