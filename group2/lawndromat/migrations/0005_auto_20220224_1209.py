# Generated by Django 2.2.5 on 2022-02-24 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawndromat', '0004_user_useraddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
