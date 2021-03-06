# Generated by Django 4.0.4 on 2022-07-12 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('road_map', '0003_pagereference_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='page_reference',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features_set', to='road_map.pagereference'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='page_references_feature',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='references_set', to='road_map.pagereferencesfeature'),
        ),
    ]
