# Generated by Django 2.1.4 on 2019-01-08 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientele', '0004_auto_20190108_2331'),
        ('psychologues', '0005_psychologues_site_web'),
    ]

    operations = [
        migrations.AddField(
            model_name='psychologues',
            name='clientele',
            field=models.ManyToManyField(blank=True, to='clientele.Clientele'),
        ),
    ]