# Generated by Django 4.0.2 on 2022-02-22 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawndromat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='money',
            field=models.IntegerField(default=0),
        ),
    ]