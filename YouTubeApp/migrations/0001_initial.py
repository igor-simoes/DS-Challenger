# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('is_positive', models.BooleanField(default=False)),
                ('time', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Thumb',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('is_positive', models.BooleanField(default=False)),
                ('time', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=40)),
                ('date_uploaded', models.DateField()),
                ('views', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='thumb',
            name='video',
            field=models.ForeignKey(to='YouTubeApp.Video'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='video',
            field=models.ForeignKey(to='YouTubeApp.Video'),
            preserve_default=True,
        ),
    ]
