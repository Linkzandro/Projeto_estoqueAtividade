# Generated by Django 5.1.4 on 2024-12-05 18:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_produto_data_criacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='data_criacao',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
