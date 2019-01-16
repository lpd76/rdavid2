# Generated by Django 2.1.4 on 2018-12-28 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('speciality', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialityDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(default=None)),
                ('speciality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='speciality.Speciality')),
            ],
        ),
    ]
