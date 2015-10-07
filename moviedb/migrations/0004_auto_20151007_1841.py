# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviedb', '0003_movie_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='rater',
            name='age',
            field=models.PositiveIntegerField(default=-1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rater',
            name='occupation',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rater',
            name='zipcode',
            field=models.CharField(default='00000', max_length=5),
            preserve_default=False,
        ),
    ]
