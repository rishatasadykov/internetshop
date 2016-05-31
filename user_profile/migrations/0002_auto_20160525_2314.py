# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import user_profile.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='site',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(null=True, upload_to=user_profile.models.get_user_image_path, blank=True),
        ),
    ]
