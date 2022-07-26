# Generated by Django 4.0.6 on 2022-07-26 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_type', models.CharField(choices=[('y', 'Y'), ('n', 'N'), ('p', 'P')], max_length=5)),
                ('recommendation', models.TextField(verbose_name='Recommendation')),
            ],
        ),
    ]
