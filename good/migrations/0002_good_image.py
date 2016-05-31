# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import good.models


class Migration(migrations.Migration):

    dependencies = [
        ('good', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='image',
            field=models.ImageField(null=True, upload_to=good.models.get_picture_path),
        ),
    ]
