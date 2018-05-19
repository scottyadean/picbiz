# Generated by Django 2.0.5 on 2018-05-13 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Directory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Name')),
                ('slug', models.CharField(max_length=255, verbose_name='Slug')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Description')),
                ('file_count', models.IntegerField(default=0, verbose_name='File Count')),
                ('create_by', models.CharField(blank=True, max_length=255, null=True, verbose_name='Created By')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
        ),
    ]
