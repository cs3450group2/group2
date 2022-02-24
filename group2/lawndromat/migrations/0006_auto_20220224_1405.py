# Generated by Django 2.2.5 on 2022-02-24 21:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('lawndromat', '0005_auto_20220224_1209'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('userZipCode', models.IntegerField()),
                ('userAddress', models.CharField(default='', max_length=100)),
                ('userType', models.CharField(max_length=50)),
                ('money', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]