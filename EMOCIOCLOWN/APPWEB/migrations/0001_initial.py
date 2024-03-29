# Generated by Django 3.0.3 on 2020-05-13 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('imagen', models.ImageField(upload_to='blog')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blog',
                'ordering': ['-fecha'],
            },
        ),
        migrations.CreateModel(
            name='Campamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True, max_length=300)),
                ('fecha_inicio', models.DateField(blank=True, null=True)),
                ('fecha_fin', models.DateField(blank=True, null=True)),
                ('imagen', models.ImageField(upload_to='campamento')),
                ('modalidad', models.CharField(default=10, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Datos_contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=12)),
                ('linkWha', models.URLField(blank=True, null=True, verbose_name='Número de whatsapp')),
                ('email', models.EmailField(max_length=50)),
            ],
            options={
                'verbose_name': 'Datos contacto',
                'verbose_name_plural': 'Datos contacto',
            },
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20)),
                ('descripcion', models.TextField(blank=True, max_length=300)),
                ('imagen', models.ImageField(upload_to='evento')),
                ('aforo', models.IntegerField(default=3, null=True)),
                ('fecha_inicio', models.DateField(blank=True, null=True)),
                ('fecha_fin', models.DateField(blank=True, null=True)),
                ('edad', models.IntegerField(default=10, null=True)),
                ('precio', models.FloatField(default=10, null=True)),
                ('modalidad', models.CharField(default=10, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True, max_length=300)),
                ('imagen', models.ImageField(upload_to='galeria')),
            ],
            options={
                'verbose_name': 'Galeria',
                'verbose_name_plural': 'Galeria',
            },
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20)),
                ('descripcion', models.TextField(blank=True, max_length=300)),
                ('imagen', models.ImageField(upload_to='personal')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Dirección Web')),
            ],
            options={
                'verbose_name': 'Info',
                'verbose_name_plural': 'Datos inicio',
            },
        ),
        migrations.CreateModel(
            name='Opiniones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True, max_length=300)),
            ],
            options={
                'verbose_name': 'Opiniones',
                'verbose_name_plural': 'Opiniones',
            },
        ),
        migrations.CreateModel(
            name='Taller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20)),
                ('descripcion', models.TextField(blank=True, max_length=300)),
                ('wasap', models.URLField(blank=True, null=True, verbose_name='Grupo de whatsapp')),
                ('imagen', models.ImageField(upload_to='taller')),
                ('modalidad', models.CharField(default=10, max_length=30)),
            ],
            options={
                'verbose_name': 'Taller',
                'verbose_name_plural': 'Talleres',
            },
        ),
    ]
