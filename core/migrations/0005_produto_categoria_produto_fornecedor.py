# Generated by Django 5.1.4 on 2024-12-12 18:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_categoria_fornecedor'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.ManyToManyField(to='core.categoria'),
        ),
        migrations.AddField(
            model_name='produto',
            name='fornecedor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.fornecedor'),
            preserve_default=False,
        ),
    ]