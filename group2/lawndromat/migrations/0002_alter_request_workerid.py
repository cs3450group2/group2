# Generated by Django 4.0.2 on 2022-03-01 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawndromat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='workerID',
            field=models.IntegerField(default=None),
        ),
    ]
