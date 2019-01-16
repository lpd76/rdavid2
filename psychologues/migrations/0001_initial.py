# Generated by Django 2.1.4 on 2019-01-04 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('speciality', '0010_auto_20190104_2001'),
        ('services', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Psychologues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='static/media/')),
                ('phone', models.CharField(blank=True, max_length=10)),
                ('fax', models.CharField(blank=True, max_length=10)),
                ('bio', models.TextField(blank=True, max_length=700)),
                ('education', models.CharField(blank=True, max_length=70)),
                ('services', models.ManyToManyField(blank=True, to='services.Service')),
                ('specialities', models.ManyToManyField(blank=True, to='speciality.SpecialityDetail')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
