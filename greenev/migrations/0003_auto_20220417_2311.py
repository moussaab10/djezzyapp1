# Generated by Django 3.1.6 on 2022-04-17 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('greenev', '0002_auto_20220417_2307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alertnotif',
            name='alert',
        ),
        migrations.RemoveField(
            model_name='alertnotif',
            name='notification_ptr',
        ),
        migrations.DeleteModel(
            name='Alert',
        ),
        migrations.DeleteModel(
            name='Alertnotif',
        ),
    ]