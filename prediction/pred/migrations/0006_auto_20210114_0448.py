# Generated by Django 2.1.15 on 2021-01-14 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pred', '0005_auto_20210114_0442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inputdata',
            name='prediction',
        ),
        migrations.AddField(
            model_name='inputdata',
            name='prediction',
            field=models.ForeignKey(default=2, on_delete='cascade', to='pred.Clasification'),
            preserve_default=False,
        ),
    ]
