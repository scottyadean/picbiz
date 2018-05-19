# Generated by Django 2.0.5 on 2018-05-17 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Name')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name_plural': 'Locations',
            },
        ),
        migrations.AddField(
            model_name='location',
            name='region',
            field=models.CharField(default=1, max_length=225, verbose_name='Region'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='section',
            field=models.CharField(default=1, max_length=225, verbose_name='Section'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mainfest',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='core_dir', to='core.Location'),
        ),
    ]