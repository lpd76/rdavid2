# Generated by Django 2.1.4 on 2019-01-09 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
        ('clientele', '0004_auto_20190108_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientele',
            name='services',
            field=models.ManyToManyField(blank=True, to='services.Service'),
        ),
    ]
