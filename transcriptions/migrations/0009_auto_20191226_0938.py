# Generated by Django 3.0 on 2019-12-26 17:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcriptions', '0008_auto_20191223_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basespeaker',
            name='speaker_label',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='project',
            name='url',
            field=models.URLField(unique=True),
        ),
        migrations.AlterField(
            model_name='transcription',
            name='settings_max_alternatives',
            field=models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(10)]),
        ),
    ]