# Generated by Django 2.2.16 on 2020-12-08 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.SlugField(unique=True, verbose_name='Nombre Clave')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('url', models.URLField(blank=True, max_length=300, null=True, verbose_name='Enlace web')),
                ('icon', models.SlugField(max_length=100, null=True, verbose_name='Icono FontAwesome')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha Actualización')),
            ],
            options={
                'verbose_name': 'Red Social',
                'verbose_name_plural': 'Redes Sociales',
                'ordering': ['name'],
            },
        ),
    ]
