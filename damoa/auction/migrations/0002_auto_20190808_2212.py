# Generated by Django 2.2.1 on 2019-08-08 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='write',
            name='confirm',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='write',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
