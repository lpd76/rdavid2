# Generated by Django 2.1.4 on 2019-01-05 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psychologues', '0004_auto_20190105_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='psychologues',
            name='site_web',
            field=models.URLField(blank=True),
        ),
    ]
