# Generated by Django 3.2.7 on 2021-10-02 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CitasVentas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordencompra',
            name='comentario',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='destinoSegundoAbono',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]