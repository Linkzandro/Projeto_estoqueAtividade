# Generated by Django 5.1.4 on 2024-12-12 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_categoria_setor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='setor',
            field=models.IntegerField(unique=True),
        ),
    ]
