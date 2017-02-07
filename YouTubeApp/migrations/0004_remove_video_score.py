# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('YouTubeApp', '0003_video_themes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='score',
        ),
    ]
