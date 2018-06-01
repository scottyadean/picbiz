# Generated by Django 2.0.5 on 2018-05-24 07:28

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('core', '0015_ui_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manifest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('caption', models.CharField(blank=True, max_length=255, null=True, verbose_name='Caption')),
                ('subject', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Subject')),
                ('sequence', models.CharField(max_length=255, verbose_name='Sequence')),
                ('thumb_path', models.CharField(max_length=500, verbose_name='Thumb Path')),
                ('src_path', models.CharField(max_length=500, verbose_name='Src Path')),
                ('import_status', models.CharField(default='init', max_length=255, verbose_name='Import Status')),
                ('date', models.DateField(verbose_name='Date')),
                ('datatime', models.DateTimeField(blank=True, null=True, verbose_name='Date Time')),
                ('height', models.CharField(blank=True, max_length=255, null=True, verbose_name='Height')),
                ('width', models.CharField(blank=True, max_length=255, null=True, verbose_name='Width')),
                ('lat', models.FloatField(default=0, verbose_name='lat')),
                ('lng', models.FloatField(default=0, verbose_name='lng')),
                ('meta_1', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='meta_1')),
                ('meta_2', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='meta_2')),
                ('meta_3', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='meta_3')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('company', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='core_manifest_company', to='core.Company')),
                ('directory', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='core_manifest_dir', to='core.Directory')),
                ('location', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='core_manifest_loc', to='core.Location')),
                ('section', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='core_manifest_section', to='core.Section')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.RemoveField(
            model_name='mainfest',
            name='company',
        ),
        migrations.RemoveField(
            model_name='mainfest',
            name='directory',
        ),
        migrations.RemoveField(
            model_name='mainfest',
            name='location',
        ),
        migrations.RemoveField(
            model_name='mainfest',
            name='section',
        ),
        migrations.RemoveField(
            model_name='mainfest',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Mainfest',
        ),
    ]