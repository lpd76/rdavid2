# Generated by Django 2.1.4 on 2019-01-10 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('speciality', '0028_auto_20190109_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialitydetail',
            name='speciality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='speciality.Speciality'),
        ),
    ]