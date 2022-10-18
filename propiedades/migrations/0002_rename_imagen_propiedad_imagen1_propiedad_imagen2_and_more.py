# Generated by Django 4.0.6 on 2022-08-12 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propiedades', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='propiedad',
            old_name='imagen',
            new_name='imagen1',
        ),
        migrations.AddField(
            model_name='propiedad',
            name='imagen2',
            field=models.ImageField(blank=True, null=True, upload_to='propiedades'),
        ),
        migrations.AddField(
            model_name='propiedad',
            name='imagen3',
            field=models.ImageField(blank=True, null=True, upload_to='propiedades'),
        ),
        migrations.AddField(
            model_name='propiedad',
            name='imagen4',
            field=models.ImageField(blank=True, null=True, upload_to='propiedades'),
        ),
    ]