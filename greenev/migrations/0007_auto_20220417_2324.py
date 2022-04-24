# Generated by Django 3.1.6 on 2022-04-17 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('greenev', '0006_auto_20220417_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alert',
            name='address',
        ),
        migrations.CreateModel(
            name='Alertnotif',
            fields=[
                ('notification_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='greenev.notification')),
                ('alert', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='greenev.alert')),
            ],
            bases=('greenev.notification',),
        ),
    ]