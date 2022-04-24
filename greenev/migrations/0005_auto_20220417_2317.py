# Generated by Django 3.1.6 on 2022-04-17 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('greenev', '0004_alert'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='cancelledReson',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='alert',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='greenev.citoyen'),
        ),
        migrations.AlterField(
            model_name='alert',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
