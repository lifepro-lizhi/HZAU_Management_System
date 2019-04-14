# Generated by Django 2.1.5 on 2019-04-13 08:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Examination', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='essay_question',
            name='title',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paper',
            name='expire_date',
            field=models.DateField(default=datetime.date(2019, 5, 13)),
        ),
    ]