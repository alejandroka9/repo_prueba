# Generated by Django 4.2.1 on 2023-06-26 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Proyectodjango', '0002_usuario'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Usuario',
            new_name='Usuarios',
        ),
    ]