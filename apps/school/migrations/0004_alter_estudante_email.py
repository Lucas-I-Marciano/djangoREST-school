# Generated by Django 5.1.4 on 2025-01-14 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_matricula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudante',
            name='cpf',
            field=models.EmailField(max_length=30, unique=True),
        ),
    ]
