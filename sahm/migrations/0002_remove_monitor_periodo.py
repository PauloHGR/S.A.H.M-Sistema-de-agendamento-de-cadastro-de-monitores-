# Generated by Django 2.0.3 on 2018-04-04 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sahm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monitor',
            name='periodo',
        ),
    ]