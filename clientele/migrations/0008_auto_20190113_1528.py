# Generated by Django 2.1.4 on 2019-01-13 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('speciality', '0036_auto_20190111_1651'),
        ('clientele', '0007_auto_20190111_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='besoin',
            name='clientele',
        ),
        migrations.RemoveField(
            model_name='besoin',
            name='probleme',
        ),
        migrations.AddField(
            model_name='clientele',
            name='probleme',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='speciality.Problematique'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Besoin',
        ),
    ]
