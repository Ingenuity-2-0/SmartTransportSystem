# Generated by Django 3.1.7 on 2021-03-30 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='businformation',
            name='bus_sourcetodestination',
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
    ]
