# Generated by Django 2.1.5 on 2019-05-16 13:33

import Video.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('upload_date', models.DateField(auto_now=True)),
                ('image', models.ImageField(upload_to=Video.models.user_directory_path)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Teacher.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('upload_date', models.DateField(auto_now=True)),
                ('video', models.FileField(upload_to=Video.models.user_directory_path)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Teacher.Teacher')),
            ],
        ),
    ]