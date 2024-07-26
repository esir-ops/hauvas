# Generated by Django 5.0.6 on 2024-07-18 22:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_semester_end_year_alter_semester_start_year'),
        ('professor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=254)),
                ('course_code', models.CharField(max_length=6)),
                ('course_codename', models.CharField(max_length=20)),
                ('course_syllabus', models.TextField()),
                ('course_unit', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_department', to='main.department')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_professor', to='professor.professor')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_semester', to='main.semester')),
            ],
        ),
    ]
