# Generated by Django 4.0.6 on 2022-08-06 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_qualifications_doctorprofile_qualification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctorprofile',
            old_name='qualification',
            new_name='qualifications',
        ),
    ]