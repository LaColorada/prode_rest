# Generated by Django 4.0.5 on 2022-06-20 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prode', '0008_match_match_end'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='tournament',
            field=models.ManyToManyField(to='prode.tournament'),
        ),
    ]