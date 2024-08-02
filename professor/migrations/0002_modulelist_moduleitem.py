# Generated by Django 5.0.6 on 2024-07-29 10:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModuleList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Week-', max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='professor.course')),
            ],
        ),
        migrations.CreateModel(
            name='ModuleItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Lesson 01', max_length=254)),
                ('description', models.TextField()),
                ('content_url', models.CharField(default='none', max_length=255)),
                ('is_published', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('module_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='professor.modulelist')),
            ],
        ),
    ]