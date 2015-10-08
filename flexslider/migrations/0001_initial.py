# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=25)),
                ('index', models.IntegerField(default=0)),
                ('descript', models.TextField(default=b'')),
                ('short_name', models.CharField(default=b'', help_text=b'short-name: no special characters, no spaces', max_length=25)),
                ('image', models.ImageField(upload_to=b'images/flexslider/', verbose_name=b'Slider image')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
