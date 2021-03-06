# Generated by Django 4.0.2 on 2022-03-01 18:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requestZip', models.IntegerField()),
                ('customerID', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('timeOfDay', models.CharField(max_length=50)),
                ('workerID', models.IntegerField()),
                ('complete', models.BooleanField(default=False)),
                ('feedBack', models.TextField()),
                ('thumbsUp', models.BooleanField(default=None)),
                ('cost', models.FloatField(default=0)),
                ('type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('userZipCode', models.IntegerField()),
                ('userName', models.CharField(max_length=100)),
                ('userAddress', models.CharField(max_length=100)),
                ('userType', models.CharField(max_length=50)),
                ('money', models.FloatField(default=0)),
            ],
        ),
    ]
