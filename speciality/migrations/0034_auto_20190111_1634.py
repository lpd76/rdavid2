# Generated by Django 2.1.4 on 2019-01-11 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speciality', '0033_auto_20190111_1631'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='problematiquetype',
            options={'ordering': ['name'], 'verbose_name_plural': 'Type de Problématique'},
        ),
        migrations.RenameField(
            model_name='specialitydetail',
            old_name='speciality',
            new_name='Type_de_Problematique',
        ),
    ]
