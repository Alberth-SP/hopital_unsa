# Generated by Django 2.2.1 on 2019-06-20 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admision', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoExamen',
            fields=[
                ('codigoTExam', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('estReg', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='ExamenLabCab',
            fields=[
                ('codigoExam', models.IntegerField(primary_key=True, serialize=False)),
                ('orden', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField()),
                ('muestra', models.CharField(max_length=100)),
                ('resultado', models.CharField(max_length=100)),
                ('valor', models.CharField(max_length=100)),
                ('observaciones', models.CharField(max_length=200)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admision.Paciente')),
                ('tipoExam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Laboratorio.TipoExamen')),
            ],
        ),
        migrations.CreateModel(
            name='ExamenLabDet',
            fields=[
                ('codigoExam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Laboratorio.ExamenLabCab')),
                ('descripcion', models.CharField(max_length=100)),
                ('resultadoObtenido', models.DateTimeField()),
                ('situacion', models.CharField(max_length=100)),
                ('rangoReferencia', models.CharField(max_length=100)),
            ],
        ),

    ]
