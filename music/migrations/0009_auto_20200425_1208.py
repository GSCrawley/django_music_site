# Generated by Django 3.0.4 on 2020-04-25 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_auto_20200425_0328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='songs',
            new_name='album',
        ),
        migrations.RemoveField(
            model_name='album',
            name='songs',
        ),
    ]
