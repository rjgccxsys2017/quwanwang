# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_remove_e_mailaddress_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('real_name', models.CharField(max_length=10)),
                ('nick_name', models.CharField(max_length=16)),
                ('accountemail', models.CharField(max_length=100)),
                ('password1', models.CharField(max_length=25)),
                ('password2', models.CharField(max_length=25)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
