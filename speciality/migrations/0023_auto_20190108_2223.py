# Generated by Django 2.1.4 on 2019-01-08 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('speciality', '0022_auto_20190105_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speciality',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='specialitydetail',
            name='speciality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='speciality.Speciality'),
        ),
    ]
