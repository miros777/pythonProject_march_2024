# Generated by Django 5.1.1 on 2024-10-02 09:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoparks', '0001_initial'),
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='autopark',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='autoparks.autoparksmodel'),
            preserve_default=False,
        ),
    ]
