# Generated by Django 4.0.5 on 2022-06-15 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prode', '0002_matchprediction_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matchprediction',
            name='score',
        ),
    ]
