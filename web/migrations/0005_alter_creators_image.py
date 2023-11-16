# Generated by Django 4.2.5 on 2023-10-03 06:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_creators_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creators',
            name='image',
            field=models.ImageField(upload_to='testimonials/', validators=[django.core.validators.FileExtensionValidator(['svg'])]),
        ),
    ]