# Generated by Django 2.1.4 on 2019-01-11 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('speciality', '0036_auto_20190111_1651'),
        ('clientele', '0006_auto_20190111_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='besoin',
            name='clientele',
        ),
        migrations.AddField(
            model_name='besoin',
            name='clientele',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='clientele.Clientele'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='besoin',
            name='probleme',
        ),
        migrations.AddField(
            model_name='besoin',
            name='probleme',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='speciality.Problematique'),
            preserve_default=False,
        ),
    ]
