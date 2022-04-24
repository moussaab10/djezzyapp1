# Generated by Django 3.1.6 on 2022-04-17 21:03

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('GradeState', models.CharField(choices=[('AUCUN', 'aucun'), ('SUPERADMAIN', 'superadmin'), ('ANALYST', 'analyste'), ('EDITEURE', 'editeur')], default='AUCUN', max_length=20)),
                ('image', models.ImageField(blank=True, default='/placeholder.png', null=True, upload_to='')),
                ('online', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EvenementState', models.CharField(choices=[('DISPO', 'disponile '), ('NOTDISPO', 'not disponible '), ('INPROGRESS', ' in progress '), ('REPORTED', 'reported ')], default='DISPO', max_length=20)),
                ('name', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('dateStart', models.DateTimeField()),
                ('address', models.TextField()),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('numReviews', models.IntegerField(blank=True, default=0, null=True)),
                ('dateUpdate', models.DateTimeField(blank=True, null=True)),
                ('dateEnd', models.DateTimeField(blank=True, null=True)),
                ('wilaya', models.CharField(max_length=50)),
                ('commune', models.CharField(max_length=50)),
                ('ville', models.CharField(max_length=50)),
                ('image1', models.ImageField(blank=True, default='/placeholder1.png', null=True, upload_to='')),
                ('image2', models.ImageField(blank=True, default='/placeholder2.png', null=True, upload_to='')),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('state', models.BooleanField(default=False, verbose_name='deja Lu')),
            ],
        ),
        migrations.CreateModel(
            name='Association',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='greenev.user')),
                ('name', models.CharField(max_length=200)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('number', models.CharField(max_length=200)),
                ('authNumber', models.CharField(max_length=200)),
                ('wilaya', models.CharField(max_length=50)),
                ('commune', models.CharField(max_length=50)),
                ('ville', models.CharField(max_length=50)),
                ('dateCreat', models.DateTimeField(default=django.utils.timezone.now)),
                ('address', models.CharField(max_length=50)),
                ('associationState', models.BooleanField(default=False)),
                ('dossiertState', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Citoyen',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='greenev.user')),
                ('number', models.CharField(max_length=200, unique=True)),
                ('evenementState', models.BooleanField(default=False)),
                ('CitezenState', models.BooleanField(default=True)),
                ('wilaya', models.CharField(max_length=50)),
                ('commune', models.CharField(max_length=50)),
                ('ville', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('nbAlert', models.IntegerField(blank=True, null=True)),
                ('nbEvenem', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alertState', models.CharField(choices=[('CANCELLED', ' cancelled'), ('ACTIVE', 'active')], default='ACTIVE', max_length=20)),
                ('cancelledReson', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('discription', models.TextField()),
                ('wilaya', models.CharField(max_length=50)),
                ('commune', models.CharField(max_length=50)),
                ('ville', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('acceptedBy', models.CharField(blank=True, max_length=200, null=True)),
                ('acceptedState', models.CharField(choices=[('NOTYET', 'not yet '), ('Accepted', 'accepted')], default='NOTYET', max_length=20)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('rating', models.IntegerField(blank=True, default=0, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('evenement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='greenev.evenement')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='greenev.citoyen')),
            ],
        ),
        migrations.CreateModel(
            name='Evenementnotif',
            fields=[
                ('notification_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='greenev.notification')),
                ('evenement', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='greenev.evenement')),
            ],
            bases=('greenev.notification',),
        ),
        migrations.AddField(
            model_name='evenement',
            name='association',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='greenev.association'),
        ),
        migrations.AddField(
            model_name='evenement',
            name='members',
            field=models.ManyToManyField(to='greenev.Citoyen'),
        ),
        migrations.CreateModel(
            name='dossier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='/placeholder.png', null=True, upload_to='')),
                ('association', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='greenev.association')),
            ],
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