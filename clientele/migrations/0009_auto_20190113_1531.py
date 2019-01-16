# Generated by Django 2.1.4 on 2019-01-13 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speciality', '0036_auto_20190111_1651'),
        ('clientele', '0008_auto_20190113_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientele',
            name='probleme',
        ),
        migrations.AddField(
            model_name='clientele',
            name='probleme',
            field=models.ManyToManyField(to='speciality.Problematique'),
        ),
    ]