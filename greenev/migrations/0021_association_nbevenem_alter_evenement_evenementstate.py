# Generated by Django 4.0.1 on 2022-04-19 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greenev', '0020_alter_review_createdat'),
    ]

    operations = [
        migrations.AddField(
            model_name='association',
            name='nbEvenem',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='evenement',
            name='EvenementState',
            field=models.CharField(choices=[('DISPO', 'disponile'), ('NOTDISPO', 'not disponible'), ('INPROGRESS', 'in progress'), ('REPORTED', 'reported'), ('CANCELLED', 'cancelled'), ('FINISHED', 'finished')], default='DISPO', max_length=20),
        ),
    ]
