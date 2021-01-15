# Generated by Django 2.1.15 on 2021-01-14 09:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pred', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inputdata',
            old_name='date',
            new_name='created',
        ),
        migrations.AddField(
            model_name='clasification',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de creación'),
            preserve_default=False,
        ),
    ]
