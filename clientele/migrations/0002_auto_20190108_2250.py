# Generated by Django 2.1.4 on 2019-01-08 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientele', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientele',
            options={'verbose_name_plural': 'clientels'},
        ),
        migrations.AlterOrderWithRespectTo(
            name='clientele',
            order_with_respect_to='nom',
        ),
    ]
