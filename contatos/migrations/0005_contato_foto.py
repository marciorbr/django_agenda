# Generated by Django 3.2.12 on 2022-03-14 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0004_rename_mostrar_contato_exibir'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/%Y/%m/'),
        ),
    ]
