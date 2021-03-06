# Generated by Django 3.1.7 on 2021-03-31 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Proceso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ordenes_procesos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField()),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orden_app.orden')),
                ('proceso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orden_app.proceso')),
            ],
        ),
        migrations.AddField(
            model_name='orden',
            name='proceso',
            field=models.ManyToManyField(through='orden_app.Ordenes_procesos', to='orden_app.Proceso'),
        ),
    ]
