# Generated by Django 4.0.5 on 2022-12-24 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ca',
            name='ca',
        ),
    ]