# Generated by Django 3.1.7 on 2021-03-02 14:54

from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0005_newslink_slug'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='newslink',
            unique_together=set([('slug', 'team')]),
        ),
    ]