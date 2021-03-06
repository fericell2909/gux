# Generated by Django 3.2.6 on 2021-08-29 03:16

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
            name='Testings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('active', models.BooleanField(default=True)),
                ('numero_rol', models.IntegerField(verbose_name='Numero de rol')),
                ('nombre_paciente', models.CharField(max_length=50, verbose_name='Nombre del paciente')),
                ('fecha_hospitalizacion', models.DateField(verbose_name='Fecha de hospitalizacion')),
                ('fecha_alta', models.DateField(blank=True, null=True, verbose_name='Fecha de alta')),
                ('fecha_prevision', models.DateField(verbose_name='Fecha de previsión')),
                ('codigo_prevision', models.CharField(max_length=50, verbose_name='Codigo de previson')),
                ('accion', models.CharField(max_length=50, verbose_name='Accion')),
                ('numero', models.IntegerField(verbose_name='Numero')),
                ('tipo_RAM', models.CharField(blank=True, max_length=50, null=True, verbose_name='tirpo_RAM')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
