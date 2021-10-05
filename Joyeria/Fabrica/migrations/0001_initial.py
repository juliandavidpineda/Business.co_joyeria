# Generated by Django 3.2.7 on 2021-10-05 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CitasVentas', '0005_auto_20211001_2201'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoMaterial', models.CharField(max_length=200)),
                ('precio', models.FloatField(default=0)),
                ('tipoUnidad', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProductoTerminado',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('tipoJoya', models.CharField(max_length=200)),
                ('manoObra', models.FloatField(default=0)),
                ('talla', models.CharField(max_length=200)),
                ('ancho', models.FloatField(default=0)),
                ('engaste', models.FloatField(default=0)),
                ('render', models.FloatField(default=0)),
                ('id_ordenCompra', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CitasVentas.ordencompra')),
                ('tipoMaterial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fabrica.material')),
            ],
        ),
        migrations.CreateModel(
            name='CuentaCobro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('oro', models.FloatField(default=0)),
                ('piedraPreciosa', models.FloatField(default=0)),
                ('manoObra', models.FloatField(default=0)),
                ('render', models.FloatField(default=0)),
                ('id_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fabrica.productoterminado')),
                ('precio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fabrica.material')),
            ],
        ),
    ]
