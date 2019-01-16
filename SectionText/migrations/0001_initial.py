# Generated by Django 2.1.4 on 2019-01-11 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SectionText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_fr', models.CharField(max_length=200, unique=True)),
                ('nom_en', models.CharField(max_length=200)),
                ('text_fr', models.TextField(max_length=1000)),
                ('text_an', models.TextField(max_length=1000)),
            ],
        ),
    ]
