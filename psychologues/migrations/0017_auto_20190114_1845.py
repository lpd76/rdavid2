# Generated by Django 2.1.4 on 2019-01-14 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psychologues', '0016_auto_20190114_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='competence',
            name='charge',
            field=models.FloatField(blank=True, default=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='competence',
            name='desc_ang',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='competence',
            name='desc_fr',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]