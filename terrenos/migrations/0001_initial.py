# Generated by Django 4.0.6 on 2022-08-12 22:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Terreno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='Terreno', max_length=20)),
                ('descripcion', models.TextField(blank=True, max_length=100, null=True)),
                ('ubicacion', models.CharField(default='Resistencia, Chaco', max_length=20)),
                ('mtscuadrados', models.IntegerField(default=0)),
                ('precio', models.IntegerField(default=0)),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imgs')),
            ],
        ),
    ]
