# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-04-16 04:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcqs', '0004_question_answer_choice_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.TextField(),
        ),
    ]
