# Generated by Django 3.2 on 2022-09-13 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0005_auto_20220913_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='fecha_creacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha de creación'),
        ),
        migrations.AddField(
            model_name='libro',
            name='fecha_creacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha de creación'),
        ),
    ]
