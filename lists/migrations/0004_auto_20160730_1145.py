# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_auto_20160728_0506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='e_mailaddress',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
