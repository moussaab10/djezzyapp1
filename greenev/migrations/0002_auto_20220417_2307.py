# Generated by Django 3.1.6 on 2022-04-17 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('greenev', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alert',
            name='acceptedBy',
        ),
        migrations.RemoveField(
            model_name='alert',
            name='address',
        ),
        migrations.RemoveField(
            model_name='alert',
            name='cancelledReson',
        ),
        migrations.RemoveField(
            model_name='alert',
            name='commune',
        ),
        migrations.RemoveField(
            model_name='alert',
            name='discription',
        ),
        migrations.RemoveField(
            model_name='alert',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='alert',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='alert',
            name='sender',
        ),
        migrations.RemoveField(
            model_name='alert',
            name='ville',
        ),
        migrations.RemoveField(
            model_name='alert',
            name='wilaya',
        ),
    ]