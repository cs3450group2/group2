# Generated by Django 3.2.12 on 2022-02-27 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawndromat', '0008_userprofile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='userAddress',
            field=models.CharField(max_length=100),
        ),
    ]