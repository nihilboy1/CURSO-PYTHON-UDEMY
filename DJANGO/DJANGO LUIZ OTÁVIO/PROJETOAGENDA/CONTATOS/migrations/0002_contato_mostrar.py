# Generated by Django 4.0.1 on 2022-01-24 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CONTATOS', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='mostrar',
            field=models.BooleanField(default=True),
        ),
    ]
