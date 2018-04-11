# Generated by Django 2.0.3 on 2018-04-07 15:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sahm', '0002_remove_monitor_periodo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monitor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='monitor',
            name='matricula',
        ),
        migrations.RemoveField(
            model_name='monitor',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='monitor',
            name='senha',
        ),
        migrations.AddField(
            model_name='monitor',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='curso',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='nascimento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='telefone',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]