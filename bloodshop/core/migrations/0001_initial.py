# Generated by Django 3.2.19 on 2023-06-17 04:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('codigoMarca', models.AutoField(primary_key=True, serialize=False, verbose_name='Código de la zapatilla')),
                ('nombreMarca', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=45)),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('contraseña', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_venta', models.DateField()),
                ('total', models.IntegerField(verbose_name=10)),
                ('estado', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Zapatilla',
            fields=[
                ('id_producto', models.IntegerField(primary_key=True, serialize=False)),
                ('nombreproduct', models.CharField(max_length=30)),
                ('tipo', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=500)),
                ('talla', models.CharField(max_length=30)),
                ('cantidad', models.IntegerField()),
                ('foto', models.ImageField(upload_to='zapatillas')),
                ('precio', models.IntegerField()),
                ('marcaproduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.marca')),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('zapatilla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.zapatilla')),
            ],
        ),
    ]
