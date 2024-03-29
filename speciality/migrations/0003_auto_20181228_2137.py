# Generated by Django 2.1.4 on 2018-12-28 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('speciality', '0002_specialitydetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialitydetails',
            name='description',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='specialitydetails',
            name='speciality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='speciality.Speciality'),
        ),
    ]
