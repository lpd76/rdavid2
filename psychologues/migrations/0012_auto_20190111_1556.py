# Generated by Django 2.1.4 on 2019-01-11 15:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speciality', '0032_auto_20190111_1556'),
        ('orientation', '0002_auto_20190109_0221'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clientele', '0005_clientele_services'),
        ('services', '0002_auto_20190109_1816'),
        ('psychologues', '0011_auto_20190111_1551'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Psychologues',
            new_name='Psychologue',
        ),
    ]
