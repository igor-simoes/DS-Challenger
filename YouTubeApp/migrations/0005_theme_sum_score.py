# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('YouTubeApp', '0004_remove_video_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='sum_score',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
    ]
