# Generated by Django 2.1.2 on 2018-10-22 08:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('memo', '0003_compttime'),
    ]

    operations = [
        migrations.AddField(
            model_name='compttime',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
