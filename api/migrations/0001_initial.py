# Generated by Django 5.0.3 on 2024-03-29 21:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HandbookCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Handbook Category',
                'verbose_name_plural': 'Handbook Categories',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='HandbookSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='api.handbookcategory')),
            ],
            options={
                'verbose_name': 'Handbook Section',
                'verbose_name_plural': 'Handbook Sections',
                'ordering': ['title'],
                'unique_together': {('title', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='HandbookEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='content_images')),
                ('video', models.URLField(blank=True, null=True)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='content_attachments')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='api.handbooksection')),
            ],
            options={
                'verbose_name': 'Handbook Entry',
                'verbose_name_plural': 'Handbook Entries',
                'ordering': ['title'],
                'unique_together': {('title', 'slug')},
            },
        ),
    ]
