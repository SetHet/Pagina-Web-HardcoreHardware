# Generated by Django 2.2.16 on 2020-11-17 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Titulo')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('image', models.ImageField(upload_to='productos')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('price', models.FloatField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.Categoria')),
            ],
            options={
                'verbose_name': 'Informacion de producto',
                'verbose_name_plural': 'Informacion de productos',
                'ordering': ['name', '-update'],
            },
        ),
    ]