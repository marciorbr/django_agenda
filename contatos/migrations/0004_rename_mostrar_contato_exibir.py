# Generated by Django 3.2.12 on 2022-03-11 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0003_auto_20220311_1912'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contato',
            old_name='mostrar',
            new_name='exibir',
        ),
    ]
