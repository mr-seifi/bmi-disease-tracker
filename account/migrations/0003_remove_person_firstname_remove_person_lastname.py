# Generated by Django 4.0.6 on 2022-07-26 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_person_options_alter_person_managers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='person',
            name='lastname',
        ),
    ]
