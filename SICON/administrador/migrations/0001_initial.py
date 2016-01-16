# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-16 21:00
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.IntegerField()),
                ('latitud', models.IntegerField()),
                ('longitud', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.IntegerField()),
                ('latitud', models.IntegerField()),
                ('longitud', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('no_documento', models.CharField(max_length=40, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('tipo_sangre', models.CharField(choices=[(b'O+', b'O+'), (b'O-', b'O-'), (b'A+', b'A+'), (b'A-', b'A-'), (b'B+', b'B+'), (b'B-', b'B-'), (b'AB+', b'AB+'), (b'AB-', b'AB-')], max_length=20)),
                ('experiencia', models.IntegerField()),
                ('jornada', models.CharField(choices=[(b'Manana', b'Ma\xc3\xb1ana'), (b'Tarde', b'Tarde'), (b'Noche', b'Noche')], max_length=15)),
                ('fecha_vinculacion', models.DateField(blank=True)),
                ('cargo', models.CharField(choices=[(b'Vendedor', b'Vendedor'), (b'Jefe de taller', b'Jefe de taller'), (b'Gerente', b'Gerente'), (b'Mecanico', b'Mec\xc3\xa1nico')], max_length=150)),
                ('telefono', models.CharField(max_length=150)),
                ('genero', models.CharField(choices=[(b'Masculino', b'Masculino'), (b'Femenino', b'Femenino')], max_length=15)),
                ('fecha_nacimiento', models.DateField()),
                ('estado_empleado', models.BooleanField(default=True)),
            ],
            options={
                'permissions': (('listar_Empleados', 'Se permite editar, activar , desactivar'),),
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('slug', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=100)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrador.Marca')),
            ],
        ),
        migrations.CreateModel(
            name='Repuesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=40, unique=True)),
                ('nombre', models.CharField(max_length=40)),
                ('marca', models.CharField(max_length=40)),
                ('costo', models.IntegerField(blank=True, null=True)),
                ('cantidad', models.IntegerField()),
                ('activo', models.BooleanField(default=True)),
                ('marca_carro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administrador.Marca')),
                ('modelo_carro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administrador.Modelo')),
            ],
            options={
                'permissions': (('listar_Repuestos', 'Se permite editar, activar , desactivar'),),
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('direccion', models.CharField(max_length=150)),
                ('telefono', models.TextField(max_length=150)),
                ('activo', models.BooleanField(default=True)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrador.Ciudad')),
            ],
            options={
                'permissions': (('listar_Sucursales', 'Se permite editar, activar , desactivar'),),
            },
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cilindraje', models.IntegerField()),
                ('marca', models.CharField(max_length=50)),
                ('linea', models.CharField(max_length=50)),
                ('modelo', models.IntegerField()),
                ('tipo_combustible', models.CharField(choices=[(b'Gasolina', b'Gasolina'), (b'Gas', b'Gas')], max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gerente',
            fields=[
                ('empleado_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='administrador.Empleado')),
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('listar_Gerente', 'Se permite editar, activar , desactivar'),),
            },
            bases=('auth.user', 'administrador.empleado'),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='JefeTaller',
            fields=[
                ('empleado_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='administrador.Empleado')),
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('listar_Jefe_Taller', 'Se permite editar, activar , desactivar'),),
            },
            bases=('auth.user', 'administrador.empleado'),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='SuperAdmin',
            fields=[
                ('empleado_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='administrador.Empleado')),
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('auth.user', 'administrador.empleado'),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='VehiculoNuevo',
            fields=[
                ('vehiculo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='administrador.Vehiculo')),
                ('valor', models.IntegerField()),
                ('codigo', models.CharField(default=1, max_length=10, unique=True)),
            ],
            options={
                'permissions': (('listar_Vehiculo_Nuevo', 'Se permite editar, activar , desactivar'),),
            },
            bases=('administrador.vehiculo',),
        ),
        migrations.CreateModel(
            name='VehiculoUsado',
            fields=[
                ('vehiculo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='administrador.Vehiculo')),
                ('servicio', models.CharField(choices=[(b'Publico', b'Publico'), (b'Prviado', b'Privado')], max_length=50)),
                ('placa', models.CharField(max_length=6, unique=True)),
            ],
            options={
                'permissions': (('listar_Vehiculo_Usado', 'Se permite editar, activar , desactivar'),),
            },
            bases=('administrador.vehiculo',),
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('empleado_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='administrador.Empleado')),
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('listar_Vendedor', 'Se permite editar, activar , desactivar'),),
            },
            bases=('auth.user', 'administrador.empleado'),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='empleado',
            name='jefe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administrador.Empleado'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='sucursal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrador.Sucursal'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrador.Departamento'),
        ),
    ]
