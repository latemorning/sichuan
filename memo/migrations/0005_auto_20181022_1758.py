# Generated by Django 2.1.2 on 2018-10-22 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0004_compttime_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compttime',
            old_name='user_id',
            new_name='user',
        ),
    ]
