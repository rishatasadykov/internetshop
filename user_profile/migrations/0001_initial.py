# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import user_profile.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('balance', models.IntegerField(default=0)),
                ('currency', models.CharField(max_length=3, choices=[(b'USD', b'USD'), (b'EUR', b'EURO'), (b'RUB', b'RUBLES')])),
                ('avatar', models.ImageField(upload_to=user_profile.models.get_user_image_path)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'userprofiles',
            },
        ),
    ]
