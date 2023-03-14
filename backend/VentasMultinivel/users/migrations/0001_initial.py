# Generated by Django 4.0.3 on 2023-03-14 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('regions', '0002_remove_region_id_alter_region_k_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='clasificacion',
            fields=[
                ('k_clasificacion', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('t_descripcion', models.CharField(max_length=15)),
                ('n_comision', models.DecimalField(decimal_places=3, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('k_usuario', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('t_email', models.CharField(max_length=50)),
                ('t_password', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='representante',
            fields=[
                ('k_representante', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('t_nombre', models.CharField(max_length=30)),
                ('t_apellido', models.CharField(max_length=30)),
                ('f_nacimiento', models.DateField()),
                ('i_genero', models.CharField(max_length=1)),
                ('n_telefono', models.DecimalField(decimal_places=0, max_digits=10)),
                ('f_contrato', models.DateField()),
                ('t_direccion', models.CharField(max_length=50)),
                ('k_clasificacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='users.clasificacion')),
                ('k_jefe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='users.representante')),
                ('k_region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='regions.region')),
                ('k_usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='users.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('k_cliente', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('t_nombre', models.CharField(max_length=30)),
                ('t_apellido', models.CharField(max_length=30)),
                ('n_telefono', models.DecimalField(decimal_places=0, max_digits=10)),
                ('k_representante', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='users.representante')),
                ('k_usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='users.usuario')),
            ],
        ),
    ]
