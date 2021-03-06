# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-31 18:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0012_auto_20160329_1126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teamcodinganswer',
            old_name='input_case_no',
            new_name='inputcase_no',
        ),
        migrations.AlterUniqueTogether(
            name='teamcodinganswer',
            unique_together=set([('team', 'question_no', 'inputcase_no')]),
        ),
    ]
