# Generated by Django 2.1.15 on 2021-01-14 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clasification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('glass', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='InputData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ri', models.IntegerField()),
                ('na', models.IntegerField()),
                ('mg', models.IntegerField()),
                ('al', models.IntegerField()),
                ('si', models.IntegerField()),
                ('k', models.IntegerField()),
                ('ca', models.IntegerField()),
                ('ba', models.IntegerField()),
                ('fe', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('prediction', models.ForeignKey(on_delete='cascade', to='pred.Clasification')),
            ],
        ),
    ]
