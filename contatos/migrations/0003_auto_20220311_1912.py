# Generated by Django 3.2.12 on 2022-03-11 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0002_alter_contato_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='mostrar',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='contato',
            name='descricao',
            field=models.TextField(blank=True, max_length=255),
        ),
    ]
