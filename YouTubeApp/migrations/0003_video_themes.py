# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('YouTubeApp', '0002_video_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='themes',
            field=models.ManyToManyField(to='YouTubeApp.Theme'),
            preserve_default=True,
        ),
    ]
