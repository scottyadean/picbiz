# Generated by Django 2.0.5 on 2018-05-15 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mainfest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Header')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Description')),
                ('import_dir', models.CharField(max_length=255, verbose_name='Import Dir')),
                ('import_status', models.CharField(default='init', max_length=255, verbose_name='Import Status')),
                ('exif_datetime', models.DateTimeField(verbose_name='exif_datetime')),
                ('exif_height', models.CharField(max_length=255, verbose_name='exif_height')),
                ('exif_width', models.CharField(max_length=255, verbose_name='exif_width')),
                ('lat', models.FloatField(default=0, verbose_name='lat')),
                ('lng', models.FloatField(default=0, verbose_name='lng')),
                ('meta_1', models.CharField(default='', max_length=255, verbose_name='meta_1')),
                ('meta_2', models.CharField(default='', max_length=255, verbose_name='meta_2')),
                ('meta_3', models.CharField(default='', max_length=255, verbose_name='meta_3')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
        ),
        migrations.AlterModelOptions(
            name='directory',
            options={'verbose_name_plural': 'Directories'},
        ),
        migrations.AddField(
            model_name='directory',
            name='full_path',
            field=models.CharField(default=1, max_length=255, unique=True, verbose_name='Full Path'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mainfest',
            name='directory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='core_dir', to='core.Directory'),
        ),
    ]
