# Generated by Django 2.1.4 on 2019-01-04 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('speciality', '0010_auto_20190104_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialitydetail',
            name='speciality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='speciality.Speciality'),
        ),
        migrations.AlterOrderWithRespectTo(
            name='speciality',
            order_with_respect_to='name',
        ),
        migrations.AlterOrderWithRespectTo(
            name='specialitydetail',
            order_with_respect_to='name',
        ),
    ]
