# Generated by Django 4.0.6 on 2022-08-13 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propiedades', '0002_rename_imagen_propiedad_imagen1_propiedad_imagen2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='propiedad',
            name='descripcion_corta',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
