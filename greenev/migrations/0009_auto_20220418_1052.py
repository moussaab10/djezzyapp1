# Generated by Django 3.1.6 on 2022-04-18 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('greenev', '0008_auto_20220418_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='acceptedBy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='greenev.association'),
        ),
        migrations.AlterField(
            model_name='alert',
            name='discription',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='alert',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='alert',
            name='ville',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
