# Generated by Django 3.2 on 2023-08-09 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telegram', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='subscriptions',
            unique_together={('user',)},
        ),
    ]
