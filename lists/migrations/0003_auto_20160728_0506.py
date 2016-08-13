# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_item_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='e_mailaddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('email', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='date pulisher')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
