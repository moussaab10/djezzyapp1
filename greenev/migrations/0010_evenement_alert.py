# Generated by Django 3.1.6 on 2022-04-18 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('greenev', '0009_auto_20220418_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='evenement',
            name='alert',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='greenev.alert'),
        ),
    ]
