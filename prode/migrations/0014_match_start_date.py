# Generated by Django 4.0.5 on 2022-06-21 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prode', '0013_remove_match_match_end_match_duration_mins'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
