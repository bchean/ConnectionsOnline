# Generated by Django 4.0.4 on 2022-05-28 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JobPostings', '0002_remove_job_job_description_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Job',
            new_name='Jobs',
        ),
    ]
