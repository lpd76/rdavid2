# Generated by Django 2.1.4 on 2019-01-09 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orientation', '0002_auto_20190109_0221'),
        ('psychologues', '0006_psychologues_clientele'),
    ]

    operations = [
        migrations.AddField(
            model_name='psychologues',
            name='orientation',
            field=models.ManyToManyField(blank=True, to='orientation.Orientation'),
        ),
    ]