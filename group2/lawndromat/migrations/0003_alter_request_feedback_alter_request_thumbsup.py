# Generated by Django 4.0.2 on 2022-03-01 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawndromat', '0002_alter_request_workerid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='feedBack',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='request',
            name='thumbsUp',
            field=models.BooleanField(default=None, null=True),
        ),
    ]
