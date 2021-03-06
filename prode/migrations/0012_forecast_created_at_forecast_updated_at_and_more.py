# Generated by Django 4.0.5 on 2022-06-21 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prode', '0011_alter_forecast_player_delete_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='forecast',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='created_at'),
        ),
        migrations.AddField(
            model_name='forecast',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='updated_at'),
        ),
        migrations.AddField(
            model_name='match',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='created_at'),
        ),
        migrations.AddField(
            model_name='match',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='updated_at'),
        ),
        migrations.AddField(
            model_name='team',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='created_at'),
        ),
        migrations.AddField(
            model_name='team',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='updated_at'),
        ),
        migrations.AddField(
            model_name='tournament',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='created_at'),
        ),
        migrations.AddField(
            model_name='tournament',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='updated_at'),
        ),
    ]
