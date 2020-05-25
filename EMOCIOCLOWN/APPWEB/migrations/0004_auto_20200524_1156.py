# Generated by Django 3.0.3 on 2020-05-24 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APPWEB', '0003_auto_20200521_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galeria',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='galeria',
            name='titulo',
        ),
        migrations.AlterField(
            model_name='blog',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='campamento',
            name='descripcion',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='campamento',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='evento',
            name='descripcion',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='info',
            name='titulo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='opiniones',
            name='descripcion',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='taller',
            name='descripcion',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='taller',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
    ]