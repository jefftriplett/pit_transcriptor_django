# Generated by Django 3.0 on 2019-12-24 04:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcriptions', '0007_auto_20191220_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basespeaker',
            name='speaker_label',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='transcription',
            name='settings_max_alternatives',
            field=models.IntegerField(blank=True, default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='transcription',
            name='settings_max_speaker_labels',
            field=models.IntegerField(blank=True, default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='transcription',
            name='status',
            field=models.CharField(choices=[('not_started', 'NOT STARTED'), ('in_progress', 'IN PROGRESS'), ('failed', 'ERROR'), ('success', 'COMPLETED'), ('pending', 'PENDING_CHANGE')], default='not_started', max_length=128),
        ),
    ]