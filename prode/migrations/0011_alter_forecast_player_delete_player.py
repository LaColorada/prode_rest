# Generated by Django 4.0.5 on 2022-06-21 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_player'),
        ('prode', '0010_remove_team_tournament'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forecast',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.player'),
        ),
        migrations.DeleteModel(
            name='Player',
        ),
    ]
