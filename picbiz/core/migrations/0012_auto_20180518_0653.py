# Generated by Django 2.0.5 on 2018-05-18 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20180517_0729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainfest',
            name='description',
        ),
        migrations.RemoveField(
            model_name='mainfest',
            name='import_dir',
        ),
        migrations.AddField(
            model_name='mainfest',
            name='caption',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Caption'),
        ),
    ]