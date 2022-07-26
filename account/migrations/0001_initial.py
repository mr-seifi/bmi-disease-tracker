# Generated by Django 4.0.6 on 2022-07-25 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(db_index=True, max_length=128)),
                ('password', models.CharField(max_length=128)),
                ('firstname', models.CharField(max_length=64)),
                ('lastname', models.CharField(max_length=64)),
                ('age', models.IntegerField(verbose_name='Age')),
                ('sex', models.CharField(choices=[('male', 'M'), ('female', 'F')], max_length=8, verbose_name='Sex')),
                ('height', models.FloatField(verbose_name='Height in cm')),
                ('weight', models.FloatField(verbose_name='Weight in Kg')),
            ],
        ),
    ]
